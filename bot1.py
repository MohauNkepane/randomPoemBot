import random
from telegram import *
from telegram.ext import *
import randomPoem as rp

import logging

MENU = 0
with open("secrets.txt", 'r') as f:
    TOKEN = f.read()
bot = Bot(TOKEN)


def start(update, context):
    update.message.reply_text("""/Poem -> To request a random Poem \n /cancel -> To Close Conversation \n/help -> To Seek Bot Help
    Please Send Me Your Location""", reply_markup=ReplyKeyboardRemove())
    return MENU


def get_user_location(update, context):
    user = update.message.from_user
    user_location = update.message.location
    update.message.reply_text("Thank You {}".format(user.first_name))
    print("{},{}".format(user_location.latitude, user_location.longitude))
    # bot.sendLocation()


def cancel(update, context):
    update.message.reply_text("Closing Conversation", reply_markup=ReplyKeyboardRemove())
    bot.close()


def help_user(update, context):
    update.message.reply_text("""
    I will guide you on how to user this bot.
    Go Back to /menu.
    """, reply_markup=ReplyKeyboardRemove())


def getPoem(update, context):
    poem = rp.stringifypoem(rp.randompoem(random.randint(0, 2972)))
    update.message.reply_text(poem, reply_markup=ReplyKeyboardRemove())
    return MENU


def main():
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    conversation_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],  #
        states={
            MENU: [
                CommandHandler("menu", start),
                CommandHandler("help", help_user),
                CommandHandler("Poem", getPoem)
            ]
        },
        fallbacks=[CommandHandler("cancel", cancel)]
    )
    dispatcher.add_handler(conversation_handler)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
