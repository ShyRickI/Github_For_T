
from pygame import *
from random import *
from copy import *
import telebot
from telebot import types # для указание типов
import config
import random
import requests
import json
#import constants

url = 'https://api.thecatapi.com/v1/images/search?mime_type=jpg'

vishnevsk =['Был отвергаем, но зато - какими!','Как горько - потерять товарный вид.','Тебя сейчас послать или по факсу?','Мадам, да вам любой уступит место!..','Ну сделай что-нибудь, хотя бы деньги!..','Срывай же все, но только не поставки!','Сейчас у нас дешевле - заплатить...','Кто ты такой, что "не припоминаешь"?!','Вложи скорей, пока ИХ не отняли!','На вашем месте я бы улетел...','Подайте на билет в Буэнос-Айрес!','В противном случае я стану с вами жить...','Как глубоко в полуночном метро...','Любимая, да ты и собеседник!..','Считайте ДЕНЬГИ - чтоб их не считать...','Как дальше жить и где ж нам парковаться?!','Довольно тут приковывать вниманье...','А удовольствия должны быть дорогими...','Готов платить, и даже знаю чем...','Да вас в виду никто и не имел!...','Я думаю, не скрыться ли с деньгами?','Мадам, да вы сама как группировка!','Порой как раз дебилы не подводят...','Зачем я так любезно согласился?','Плачу за все - и все же в неоплатном...','Ну можно ль полагаться на живых?','О, как подорожало одолженье!','"ХАЛЯВА" нам и даром не нужна...','Во что же верить, вкладывать наличность?!','Вы что, мужчина, Вы не из Ламанчи?..','...Чем Вам, уж лучше в руки Правосудия!..','Ничто не помешает вам отвлечься..','Скажу как иномарка иномарке...','Таких как Вы, из лейки поливал бы...','По телефону смотритесь вы лучше...','Для вас не жаль и брокерского места!..','В отличье от себя - тебе я верю!..','Со словом "однозначно" - осторожней...','А Вас я попрошу упасть ничком...','Дай мне хоть что-то, кроме установок!..','Я в душу вам?! о я же не доплюну!..','Хочу понять, чего бы вы хотели...','Пройдут года и вас я захочу...','Устал решать посильные задачи...','Ну вот, опять я выручил страну!..','Да, Вы, милорд, увы, не слаще редьки...','Застать Вас на работе - как застукать..','Вы правы, да, на "Вы" гигиеничней...','А грамотно я всех вас раскидал!','Не поднял я перчатки вашей рваной...','Я что-то тут событием не стал...','Вот роскошь - отказаться от круиза...','Зачем о вас, давайте о приятном!','Сегодня нет напрасных опасений...','Да не реви, ведь я тебя смешу!..','Что может быть крупнее неприятностей?','Ну что, еще и вами заниматься?!','О, где б я ни был, рвусь в другое место!..','Там будет все, чего тебе нельзя..','Здесь нестабильно даже ухудшенье...']

random_message = lambda: random.choice(vishnevsk)

token='5570068886:AAFYxm-BItCqTKmY9rYjlYS9npP46pK_sWA'
bot = telebot.TeleBot(token)

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url2 = contents['url']
    return url2


name = str()
@bot.message_handler(commands = ['go'])
def send_pool(message):
    new = 'Как погода?'
    com = message.text.split()
    del com[com.index('/go')]
    com.append(new)
    answers = ['Классная!','Ну так себе','Бывало лучше...']
    bot.send_poll(message.chat.id, new, answers)
    print(com)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🐱 Кот")
    btn2 = types.KeyboardButton("🐕 Собака")
    btn3 = types.KeyboardButton("🎲 Рандомайзер")
    btn4 = types.KeyboardButton("© Паста")
    btn5 = types.KeyboardButton("❓ Опрос")

    markup.add(btn1, btn2, btn3, btn4, btn5)

    bot.send_message(message.chat.id, text="Привет. Я бот для поднятия настроения".format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "🐱 Кот"):

        response = requests.get(url)
        data = response.json()
        cat = data[0]['url']

        bot.send_photo(message.chat.id, cat)

    elif(message.text == "🐕 Собака"):
        #response2 = requests.get(url2)
        #data2 = response2.json()
        #dog = data2[0]['url']
        #bot.send_photo(message.chat.id, dog)

        url3 = get_url()
        bot.send_photo(message.chat.id,photo=url3)

    elif(message.text == "© Паста"):
        bot.send_message(message.chat.id, random_message())

    elif(message.text == "❓ Опрос"):
        new = 'Как погода?'
        com = message.text.split()
        del com[com.index('Опрос')]
        com.append(new)
        answers = ['Классная!','Ну так себе','Бывало лучше...']
        bot.send_poll(message.chat.id, new, answers)


    elif(message.text == "🎲 Рандомайзер"):

        bot.send_message(message.chat.id, 'Введите аргументы:')
        bot.register_next_step_handler(message, car_name)

def car_name(message):

            command = message.text.split(" ")
            command_len = len(command)
            try:
                if command_len == 1:
                    bot.reply_to(message, random.randint(1,100))
                elif command_len == 2:
                    bot.reply_to(message, random.randint(1, int(command[1])))
                elif command_len == 3:
                    bot.reply_to(message, random.randint(int(command[1]), int(command[2])))
                else:
                    bot.reply_to(message, "Максимальна кількість параметрів - 2.")
            except Exception:
                bot.reply_to(message, "Щось пішло не так, спробуйте знову.")






bot.polling(none_stop=True)

