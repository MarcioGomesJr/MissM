
from telegram.ext import Updater, CommandHandler
from commands import start, task, completeTask, greetings
from tele_token import TOKEN

# Falta implementar Job, Webcrawler, RASA NLU
if __name__ == "__main__":

    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('complete', completeTask))
    dispatcher.add_handler(CommandHandler('list', greetings))   
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('task', task))
    updater.start_polling()
    updater.idle()
