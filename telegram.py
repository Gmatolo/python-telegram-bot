import telegram
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
# from telegram.ext.commandhandler import CommandHandler
# from telegram.ext.messagehandler import MessageHandler
# from telegram.ext.filters import Filters




bot_token = "5428090458:AAEx_rqQ8nAGdl0_PTX0UJRImjZZ-ZIm38o"
bot_user_name = "wingu_safi_bot"
URL = "the heroku app link that we will create later"


updater = Updater(bot_token,
				use_context=True)


def start(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Enter the text you want to show to the user whenever they start the bot")
