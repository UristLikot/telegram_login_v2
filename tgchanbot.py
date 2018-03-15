from telegram.ext import CommandHandler,MessageHandler,Updater
updater = Updater(token='BOT_TOKEN')
dispatcher = updater.dispatcher

def startCommand(bot,update):
    bot.send_message(chat_id=update.message.chat_id,text='Hello')
    usr_id=(update.message.chat.id)
    bot.send_message(chat_id=update.message.chat_id, text=usr_id)


def start_bot():
    start_command_handler = CommandHandler('start', startCommand)
    dispatcher.add_handler(start_command_handler)
    updater.start_polling(clean=True)
