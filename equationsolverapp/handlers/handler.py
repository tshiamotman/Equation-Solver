from email import message
from telegram.ext import CallbackContext
from telegram import Update
from equationsolverapp.handlers.calculator import Calculator

from equationsolverapp.models import User


def calculator_handler(update: Update, context: CallbackContext) -> None:
    [command, equation] = str(update.message.text).split(" ", 1)
    
    if command == "solve":
        calculator = Calculator(equation)
        text = f"The following steps will help to solve {calculator.get_equation_string()}"    

        text += "\n\nStep 1\nMove the unknowns on the right to the left\nThe following should be moved:"

        for var in calculator.move_unknowns_to_left_expression():
            text += f"\n    {var.__str__()}"

        text += "\n\nStep 2\nMove the variables without unknowns to the left\nThe following should be moved:"
        
        for var in calculator.move_numbers_to_right_expression():
            text += f"\n    {var.__str__()}"

        sum_of_unknown = calculator.sum_unknowns()
        
        text += f"\n\nStep 3\nSum all the unknowns to get the following: "
        text += f"{'-' if sum_of_unknown.sign == -1 else ''}{sum_of_unknown.__str__()}"
        text += f"\n    {calculator.get_equation_string()}"

        sum_of_numbers = calculator.add_numbers()

        text += f"\n\nStep 4\nSum all the numbers to get the following: "
        text += f"{'-' if sum_of_numbers.sign == -1 else ''}{sum_of_numbers.__str__()}"
        text += f"\n    {calculator.get_equation_string()}"

        value_of_unknown = calculator.solve_value_of_unknown()

        text += f"\n\nStep 5\nDivide both sides with {sum_of_unknown.get_actual_number()}"

        text += f"\n    {sum_of_unknown.unknown} = {value_of_unknown}"

    else:
        text = "Please send 'solve <equation>' to get steps to solve equation"

    update.message.reply_text(text= text)


def help_handler(update: Update, context: CallbackContext) -> None:
    text = "'solve <equation>' to get steps to solve equation"
    update.message.reply_text(text= text)


def error_handler(update: Update, context: CallbackContext):
    print(f"Update {update} caused error {context.error}")


def command_start(update: Update, context: CallbackContext) -> None:
    u, created = User.get_user_and_created(update, context)

    if created:
        text = "Hello {first_name}".format(first_name=u.first_name)
    else:
        text = "Welcome back, {first_name}".format(first_name=u.first_name)

    text += "\n \nSend '/help' to get help"

    update.message.reply_text(text=text)




