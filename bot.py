from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = "8556188183:AAHcexoCysN-GYDiCTRf6XkHLlOWtRjyj_k"

def start(update, context):
    update.message.reply_text("Hi 👋 I am alive!")

def reply(update, context):
    update.message.reply_text("You said: " + update.message.text)

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, reply))

updater.start_polling()
updater.idle()
