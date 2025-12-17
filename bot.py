import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Bot token will come from Render environment variable
TOKEN = os.getenv("BOT_TOKEN")

def start(update, context):
    update.message.reply_text("Hi 👋 I am alive!")

def reply(update, context):
    update.message.reply_text("You said: " + update.message.text)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, reply))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
