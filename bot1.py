import os
from telegram import *
from telegram.ext import *
import randomPoem as rp
from dotenv import load_dotenv
load_dotenv()

MENU = 0


bot = Bot(os.getenv("TOKEN"))


def start(update, context):
    update.message.reply_text("""/Poem -> To request a random Poem \n /cancel -> To Close Conversation \n/help -> To Seek Bot Help
    Please Send Me Your Location""", reply_markup=ReplyKeyboardRemove())
    return MENU


def cancel(update, context):
    update.message.reply_text("Closing Conversation", reply_markup=ReplyKeyboardRemove())
    ConversationHandler.END


def help_user(update, context):
    update.message.reply_text("""
    I will guide you on how to user this bot.
    Go Back to /menu.
    """, reply_markup=ReplyKeyboardRemove())
    start(update, context)


def getPoem(update, context):
    poem = rp.stringifypoem(rp.randompoem())
    update.message.reply_text(poem, reply_markup=ReplyKeyboardRemove())
    start(update, context)



def main():
    print("The bot is currently online...")
    updater = Updater(os.getenv("TOKEN"))
    dispatcher = updater.dispatcher

    conversation_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],  #
        states={
            MENU: [
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
