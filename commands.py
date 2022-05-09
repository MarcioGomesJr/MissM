
from telegram.ext import CallbackContext
from telegram import *
from user_database import saveTask, saveUser, fetchTasks, deleteTask


def start(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_chat.id, text= "Olá! Meu nome é Ms. M, sua assistente pessoal. Prometo tentar atendê-lo da melhor forma possível :)")
    user = update.message.from_user
    saveUser(user.id, user.first_name, user.username)

def task(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    task = update.message.text.replace('/task ', '')
    saveTask(user.id, task)
    context.bot.send_message(chat_id=update.effective_chat.id, text='Lembrete anotado com sucesso! Tudo nos conformes, te avisarei no começo do dia ;)')

def greetings(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    tasks = list(fetchTasks(user.id))
    context.bot.send_message(chat_id=update.effective_chat.id, text='Bom dia! Seus lembretes de hoje são:')
    for x in range(len(tasks)):
        task = tasks[x][1]
        context.bot.send_message(chat_id=update.effective_chat.id, text = f'{task}')

def completeTask(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    task = update.message.text.replace('/complete ', '')
    print(type(task))
    deleteTask(user.id, task)
    context.bot.send_message(chat_id=update.effective_chat.id, text='Lembrete apagado!')
