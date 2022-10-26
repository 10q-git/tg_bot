# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import telebot
from telebot import types
import json

chel = ''
bot = telebot.TeleBot('5675141440:AAGYQbAstLWPB1_h_YI_Vfdhszz_CGS-4Ns')

@bot.message_handler(commands=['start'])
def start(message):
    if message.chat.type == 'group':
        bot.send_message(message.chat.id, "Type <b>/who</b> for choose new slave)", format('html'))
    if message.chat.type == 'private':
        bot.send_message(message.chat.id, "Help", format('html'))

@bot.message_handler(commands=['who'])
def who(message):
    with open("data.json", "r") as file:
        group = json.load(file)
        sorted_keys = sorted(group, key=group.get)
        bot.send_message(message.chat.id, sorted_keys[0])

@bot.message_handler(commands=['stat'])
def stat(message):
    with open("data.json", "r") as file:
        group = json.load(file)
        stat_str = ''
        for chel in group.keys():
            stat_str += chel + ' ' + str(group[chel]) + '\n'
        bot.send_message(message.chat.id, stat_str, reply_markup=types.ReplyKeyboardRemove())
@bot.message_handler(commands=['add'])
def add(message):
    with open("data.json", "r") as file:
        group = json.load(file)
        if message.chat.type == 'private':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            i = 0
            group_button = list()
            for chel in group.keys():
                group_button.append(types.KeyboardButton(chel))
                if (i % 3 == 2):
                    markup.add(group_button[i-2], group_button[i-1], group_button[i])
                if (i == len(group) - 1):
                    if (i % 3 == 1):
                        markup.add(group_button[i-1], group_button[i])
                    if (i % 3 == 0):
                        markup.add(group_button[i])
                i += 1
            bot.send_message(message.chat.id, "Choose slave", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text(message):
    with open("data.json", "r") as file:
        group = json.load(file)
        global chel
        if message.chat.type == 'private':
            if message.text in '12345' and chel != '':
                group[chel] += int(message.text)
                stat = ''
                for chel in group.keys():
                    stat += chel + ' ' + str(group[chel]) + '\n'
                bot.send_message(message.chat.id, stat, reply_markup=types.ReplyKeyboardRemove())
            for chel in group.keys():
                if chel == message.text:
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=5)
                    but1 = types.KeyboardButton('1')
                    but2 = types.KeyboardButton('2')
                    but3 = types.KeyboardButton('3')
                    but4 = types.KeyboardButton('4')
                    but5 = types.KeyboardButton('5')
                    markup.add(but1, but2, but3, but4, but5)
                    bot.send_message(message.chat.id, "How served?", reply_markup=markup)
                    break

    with open('data.json', 'w') as file:
        file.write(json.dumps(group))
bot.polling(none_stop=True)