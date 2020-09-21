#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hello friend!')


def help_command(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Hello I am here to help you !')

def image_extracter(update, context):
    file_name = 'test.jpg'
    file_id = update.message.photo[-1].file_id
    newFile = context.bot.get_file(file_id)
    newFile.download(file_name)
    update.message.reply_text('Ok i got your image')

    # Simple image to string
    extracted_text = (pytesseract.image_to_string(Image.open(file_name)))
    update.message.reply_text(extracted_text)
    


def echo(update, context):
    """Echo the user message."""
    text_received = update.message.text
    list_string = text_received.split()
    for text in list_string:
        
        if text == 'cement':
            update.message.reply_text('Ok noted ...I will arrange')
    if text !='cement':
        update.message.reply_text('Message notted ')


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1074428108:AAFGTrkmsrHsqAY8EPVo6gKnrd4-icVO6UE", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    dp.add_handler(MessageHandler(Filters.photo, image_extracter))
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()