import telegram.error
from telegram import Bot, Update, BotCommand
from telegram.ext import (
    Updater, Dispatcher, Filters, CommandHandler, MessageHandler, CallbackQueryHandler
)

def setup_dispatcher(dp):
    
    dp.add_handler(CommandHandler("start", ))
