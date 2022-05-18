from telegram.ext import updater, CommandHandler, MessageHandler, Filters

token = "5380759989:AAEeGS-P-iNzM1Cs-oba1s6FgaGKTxM4Ug8"


def on_start(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text="Привет!")


updater = Updater(token, use_context=True)

dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler("start", on_start))
dispatcher.add_handler(MessageHandler(Filters.all, on_message))

updater.start_polling()
updater.idle()
