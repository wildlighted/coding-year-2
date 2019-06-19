import telebot
from telebot import types
import random
import textsfromlastnight
import os
BOT_TOKEN = os.environ["BOT_TOKEN"]

telebot.apihelper.proxy = {
    'https': 'socks5h://geek:socks@t.geekclass.ru:7777'}
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    keyboard_1 = types.ReplyKeyboardMarkup(row_width=2)
    sms = types.KeyboardButton('Давай смску!')
    play = types.KeyboardButton('Хочу сыграть!')
    stop = types.KeyboardButton('Стоп, надоело.')
    keyboard_1.add(sms, play, stop)
    bot.send_message(message.chat.id,
                     "Привет! Я бот, который генерирует для вас "
                     "пьяные смски на основе сайта textsfromlastnight.com\n"
                     "Это 5500 страниц сообщений, примерно столько же "
                     "текста, сколько в серии книг о Гарри Поттере. Вы "
                     "можете читать и наслаждаться, а можете попробовать "
                     "угадать, настоящая ли перед вами смска. Вперед!",
                     reply_markup=keyboard_1)

@bot.message_handler(func=lambda x: x.text in ['Давай смску!', 'Еще одну',
                                               'Давай дальше!', 'Хочу еще!',
                                               'Окей, хочу почитать!'])
def send_generated_text(message):
    keyboard_2 = types.ReplyKeyboardMarkup(row_width=2)
    more_sms = types.KeyboardButton(
        random.choice(['Еще одну!', 'Давай дальше!',
                       'Хочу еще!']))
    now_play = types.KeyboardButton('Хватит, давай сыграем!')
    stop_1 = types.KeyboardButton('Горшочек, не вари!')
    keyboard_2.add(more_sms, now_play, stop_1)
    bot.send_message(message.chat.id, textsfromlastnight.make_text('clean.txt'),
                     reply_markup=keyboard_2)

@bot.message_handler(func=lambda x: x.text in ['Хватит, давай сыграем!',
                                               'Хочу сыграть!',
                                               'Еще разок!', 'Играем дальше!'])
def guess_one(message):
    keyboard_3 = types.ReplyKeyboardMarkup(row_width=2)
    btn1 = types.KeyboardButton('1')
    btn2 = types.KeyboardButton('2')
    keyboard_3.add(btn1, btn2)
    global real_text
    global choice
    real_text = textsfromlastnight.choose_text('clean.txt')
    fake_text = textsfromlastnight.make_text('clean.txt')
    choice = [real_text, fake_text]
    random.shuffle(choice)
    bot.send_message(message.chat.id, f'Ну, что написал человек?\n\n'
                     f'1: {choice[0]}\n2: {choice[1]}', reply_markup=keyboard_3)

@bot.message_handler(func=lambda x: x.text in ['1', '2'])
def answer(message):
    keyboard_4 = types.ReplyKeyboardMarkup(row_width=2)
    more_play = types.KeyboardButton(
        random.choice(['Еще разок!', 'Играем дальше!']))
    now_sms = types.KeyboardButton('Окей, хочу почитать!')
    stop_2 = types.KeyboardButton('Все, больше не хочу.')
    keyboard_4.add(more_play, now_sms, stop_2)
    if choice[int(message.text)- 1] == real_text:
        bot.send_message(message.chat.id, 'Точно! Это человек.',
                         reply_markup=keyboard_4)
    else:
        bot.send_message(message.chat.id, 'Нет, это я придумал!',
                         reply_markup=keyboard_4)

@bot.message_handler(func=lambda x: x.text in ['Стоп, надоело.',
                     'Все, больше не хочу.', 'Горшочек, не вари!'])
def goodbye(message):
    bot.send_message(message.chat.id, 'Хорошо, пока! Чтобы начать заново, '
                                      'нужно написать мне /start')

if __name__ == '__main__':
    bot.polling(none_stop=True)
