from telegram.ext import CommandHandler, Updater
from telegram import Bot, Chat,TelegramError

updater = Updater(token='BOT_API')
bot = updater.dispatcher.bot


def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Hello')
    cht_id = update.message.chat_id
    #add user id to DB
    return cht_id #user id
def check_group(bot,channe_name):
    try:
        check=Bot.getChat(bot,chat_id=channe_name)
        return check
    except (TelegramError):
        pass
def check_group_admin(bot, channel_name):
    try:
        adm = Bot.getChatAdministrators(bot, chat_id=channel_name)
        for key in adm:
            s = key.user.id
            str=[]
            str.append(s)
            return str
    except (TelegramError):
        pass


def start_bot():
    start_command_handler = CommandHandler('start', startCommand)
    updater.dispatcher.add_handler(start_command_handler)
    updater.start_polling(clean=True)
