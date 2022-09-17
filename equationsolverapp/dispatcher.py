import logging
import sys
import telegram.error
from telegram import Bot, Update
from equationsolver.celery import app
from telegram.ext import (
    Updater, Dispatcher, CommandHandler, MessageHandler,Filters
)
from equationsolver.settings import DEBUG, TELEGRAM_TOKEN
from equationsolverapp.handlers.handler import command_start, calculator_handler, error_handler


def setup_dispatcher(dp: Dispatcher):
    
    dp.add_handler(CommandHandler("start", command_start))

    dp.add_handler(CommandHandler("help", calculator_handler))

    dp.add_handler(MessageHandler(Filters.text, calculator_handler))

    # dp.add_error_handler(error_handler)


def run_polling():
    """ Run bot in polling mode """
    updater = Updater(TELEGRAM_TOKEN, use_context=True)

    dp = updater.dispatcher
    dp = setup_dispatcher(dp)

    bot_info = Bot(TELEGRAM_TOKEN).get_me()
    bot_link = f"https://t.me/" + bot_info["username"]

    print(f"Polling of '{bot_link}' has started")
    # it is really useful to send '👋' emoji to developer
    # when you run local test
    # bot.send_message(text='👋', chat_id=<YOUR TELEGRAM ID>)

    updater.start_polling()
    updater.idle()


# Global variable - best way I found to init Telegram bot
bot = Bot(TELEGRAM_TOKEN)
try:
    TELEGRAM_BOT_USERNAME = bot.get_me()["username"]
except telegram.error.Unauthorized:
    logging.error(f"Invalid TELEGRAM_TOKEN.")
    sys.exit(1)


@app.task(ignore_result=True)
def process_telegram_event(update_json):
    update = Update.de_json(update_json, bot)
    dispatcher.process_update(update)


n_workers = 0 if DEBUG else 4
dispatcher = setup_dispatcher(Dispatcher(bot, update_queue=None, workers=n_workers, use_context=True))
