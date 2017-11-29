from telegram.ext import Updater, CommandHandler, MessageHandler, Filters #импортирует нужные компоненты
import logging
#import ephem
import datetime
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )
def new_user(bot, update): #C
    text = 'Вызван /start'
    print(text)
    update.message.reply_text('Вызван /start')


def talk_to_me(bot, update): #M
    user_text = update.message.text
    logging.info(user_text)
    update.message.reply_text(user_text)


def count(bot, update, args): #C
    user_text = args
    logging.info(user_text)
    if (args[0][0] and args[-1][-1]) != '"':
        print("Сообщение должно быть заключено в двойные кавычки")
        update.message.reply_text("Сообщение должно быть заключено в двойные кавычки")
    for element in user_text:
        if element == ",":
            print("Сообщение должно содержать корректное значение")
            update.message.reply_text("Сообщение должно содержать корректное значение")
            return 1
    logging.info(user_text)
    update.message.reply_text(len(user_text))


def calculator(bot, update, args): #C
    user_text = args
    logging.info(user_text)
    if (args[0][0] and args[-1][-1]) != '"':
        print("Сообщение должно быть заключено в двойные кавычки")
        update.message.reply_text("Сообщение должно быть заключено в двойные кавычки")
    for element in user_text:
        if "=" in element:
            calc = args[:-2]
            if "/0" in calc:
                print("Нельзя делить на 0")
                return 1
            print(exec('{0}.format(calc)'))
        else:
            print("Сообщение должно заканчиваться знаком '='")
            update.message.reply_text("Сообщение должно заканчиваться знаком '='")
            return 1
    logging.info(user_text)
    update.message.reply_text(len(user_text))


def planets(first):
        planet1 = ephem.Mars()
        print(exec('{0} = ephem.{0}()'.format(first)))
        print(exec('{0}'.format(first)))
        print('ephem.{0}()'.format(first))
#planets(input ("Enter the name of planet: "))


def main():
    updater = Updater("489495136:AAG1YomFQgzb7sDMMXrYkAaGcVSP26t7ZWg")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", new_user))
    #dp.add_handler(CommandHandler("planets", first))
    dp.add_handler(CommandHandler("wordcount", count, pass_args=True))
    #dp.add_handler(MessageHandler(Filters.text, calculator, pass_args=True))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    updater.start_polling() #ходит и спрашивает телеграм - есть что для меня?
    updater.idle() #Ходить до тех пор, пока его не остановят
main()
