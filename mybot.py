from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from telegram import *
from telegram.ext import * 
from requests import *

updater = Updater("5346368485:AAFHpaZzzUolArLAvImfV4-mVpE_u4W3rj8",
				use_context=True)
#randomImageText = "Random Image"

def start(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Hello, Welcome. Please write\
		/help to get PDF")
	#buttons = [[KeyboardButton(randomImageText)]]

def help(update: Update, context: CallbackContext):
	update.message.reply_text("""To get access to the PDF, You have to complete the following work :-
	/youtube - Subscribe to Youtube channel and Like
	/telegram - Join to this Telegram channel
	/facebook - Follow this Facebook page
	/screen_shot - Send me the screenshot after you campleted the above 3 task and I will send you immediately after confirmed""")


def telegram_url(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Join this telegram channel by this link =>\
		https://t.me/Csolve1")


def youtube_url(update: Update, context: CallbackContext):
	update.message.reply_text("To Subscribe Click this Youtube Link and send me Screenshot after Subscribed =>\
	https://www.youtube.com/channel/UCWDFRw4SQ06K--RkF2YVIQA")


def facebook_url(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Follow this facebook page send me Screenshot after Followed => \
		https://www.facebook.com/csolveoro")

def file_url(update: Update, context: CallbackContext):
	update.message.reply_text(
            "Send me the screenshot after you campleted the above task to =>\
            https://t.me/ararso2")
		

def unknown(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Sorry '%s' is not a valid command" % update.message.text)


def unknown_text(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Sorry I can't recognize you , you said '%s'" % update.message.text)


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('youtube', youtube_url))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('facebook', facebook_url))
updater.dispatcher.add_handler(CommandHandler('telegram', telegram_url))
updater.dispatcher.add_handler(CommandHandler('Screen_shot', file_url))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
	Filters.command, unknown)) # Filters out unknown commands

# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()
