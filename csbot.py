from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                         RegexHandler, ConversationHandler)
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove

STATE1 = 1
STATE2 = 2

def welcome(update, context):
    message = "Olá, " + update.message.from_user.username + "!"
    print(message)
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def Indice(update, context):
    message = '''escolha qual indice você quer visualizar: \n'
        1 - Filmes \n
        2 - Séries'''
    update.message.reply_text(message, reply_markup=ReplyKeyboardMarkup([], one_time_keyboard=True)) 
    return STATE1

def inputIndice(update, context):
    Indice = lower(update.message.text)
    print(Indice)
    if (Indice == '1' or Indice == 'filmes'):
        message = '''esses são os filmes que já foram postados. \n
                        Em breve novas atualizações.'''
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        return STATE2
    else:
        if (Indice == '2' or Indice == 'séries'):
            message = '''essas são as séries que já foram postadas. \n
                        Em breve novas atualizações.'''
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        return STATE2

def inputPedidos(update, context):
    Pedidos = update.message.text
    message = "Faça seu pedido, podendo ser filme ou série, para facilitar a busca, insira nome original e se possivel o ano."
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def cancel(update, context):
    return ConversationHandler.END

def main():
    token = '1435564394:AAHDbOjsjxCqSOBSWnZWYbGp_NH3Xj-Xquk'
    updater = Updater(token=token, use_context=True)
    
    updater.dispatcher.add_handler(CommandHandler('start', welcome))

    conversation_handler = ConversationHandler(
        entry_points=[CommandHandler('Indice', Indice)],
        states={
            STATE1: [MessageHandler(Filters.text, inputIndice)],
            STATE2: [MessageHandler(Filters.text, inputPedidos)]
        },
        fallbacks=[CommandHandler('cancel', cancel)])
    updater.dispatcher.add_handler(conversation_handler)

    updater.start_polling()
    print('Olá, msg de teste' + str(updater))
    updater.idle()

if __name__ == '__main__':
    main()
