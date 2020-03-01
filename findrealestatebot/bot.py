import telebot
import config
from telebot import types
import db
import scrapper

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    print(f'Received message: {message.text} from user {message.from_user.username}')

    #keabord
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(types.InlineKeyboardButton('Buy property', callback_data='buy'),
               types.InlineKeyboardButton('Rent property', callback_data='rent'))

    bot.send_message(message.chat.id,
                     f'Hello, {message.from_user.username}!\nThis is FindRealEstateBot. Here you can find any type of property you want!',
                    reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # try:
    if call.message:
        if call.data == 'buy':
            search_type = 'buy'
            print(call.message.chat)
            db.create_record(call.message.chat.username, search_type)

            bot.send_message(call.message.chat.id, f'Ok. How many bedrooms do you want?')
            bot.register_next_step_handler(call.message, get_beds_num)

        elif call.data == 'rent':
            search_type = 'rent'
            print(call.message.chat.username)

            db.create_record(call.message.chat.username, search_type)


            bot.send_message(call.message.chat.id, f'Ok. How many bedrooms do you want?')
            bot.register_next_step_handler(call.message, get_beds_num)

        elif call.data == 'correct':
            user = db.get_user(call.message.chat.username)
            search_type = user['search_type']
            beds = user['beds']
            baths = user['baths']
            min_price = user['min_price']
            max_price = user['max_price']

            data = scrapper.get_results(search_type, beds, baths, min_price, max_price)

            bot.send_message(call.message.chat.id, f'Ok. Here is available variants')
            for el in data[0:10]:
                bot.send_message(call.message.chat.id, f'Price: {el["price"]}\nSize: {el["size"]}\nLocation: {el["location"]}\nLink: {el["link"]}')

            bot.send_message(call.message.chat.id, 'Thanks for using FindRealEstateBot.\nMade by Burik Sergio @sergioburik')


        elif call.data == 'incorrect':
            bot.send_message(call.message.chat.id, f'Ok. How many bedrooms do you want?')
            bot.register_next_step_handler(call.message, get_beds_num)

    # except Exception as e:
    #     print(repr(e))

def get_beds_num(message):
    while int(db.get_user(message.from_user.username)['beds']) == 0:
        try:
            if int(message.text) <= 0:
                bot.send_message(message.chat.id, 'Number of beds cannot be less than zero')
            elif int(message.text) > 6:
                bot.send_message(message.chat.id, 'It should be very big house, please try again')
            else:
                beds = int(message.text)

                db.update_data(message.from_user.username, 'beds', beds)

                bot.send_message(message.chat.id, 'Write how many bathrooms do you want.')
                bot.register_next_step_handler(message, get_baths_num)
        except Exception as e:
            print(e)
            bot.send_message(message.chat.id, 'Number of beds, please')

def get_baths_num(message):
    while int(db.get_user(message.from_user.username)['baths']) == 0:
        try:
            if int(message.text) <= 0:
                bot.send_message(message.chat.id, 'Number of baths cannot be less than zero')
            elif int(message.text) > 6:
                bot.send_message(message.chat.id, 'It should be very big house, please try again')
            else:
                baths = int(message.text)

                db.update_data(message.from_user.username, 'baths', baths)

                bot.send_message(message.chat.id, "Write the minimum price.")
                bot.register_next_step_handler(message, get_minimum_price)

        except Exception as e:
            bot.send_message(message.chat.id, 'Number of baths, please')

def get_minimum_price(message):
    while int(db.get_user(message.from_user.username)['min_price']) == -1:
        try:
            min_price = int(message.text) if int(message.text) >= 0 else bot.send_message(message.chat.id, 'Please, enter correct price')

            db.update_data(message.from_user.username, 'min_price', min_price)

            bot.send_message(message.chat.id, "Write the maximum price.")
            bot.register_next_step_handler(message, get_maximum_price)
        except Exception as e:
            pass


def get_maximum_price(message):
    while int(db.get_user(message.from_user.username)['max_price']) == -1:
        try:
            max_price = int(message.text) if int(message.text) >= 0 else bot.send_message(message.chat.id,
                                                                                          'Please, enter correct price')

            db.update_data(message.from_user.username, 'max_price', max_price)
            user = db.get_user(message.from_user.username)
            search_type = user['search_type']
            beds = user['beds']
            baths = user['baths']
            min_price = user['min_price']
            max_price = user['max_price']

            markup = types.InlineKeyboardMarkup(row_width=2)
            markup.add(types.InlineKeyboardButton('Yes', callback_data='correct'),
                       types.InlineKeyboardButton('No', callback_data='incorrect'))

            bot.send_message(message.chat.id,
                             f'You want to {search_type} Property\nCity: San Fransico\nBeds: {beds}\nBaths: {baths}\nMin Price: {min_price}\nMax Price: {max_price}\n',
                             reply_markup=markup)

        except Exception as e:
            print(e)

# @bot.message_handler(content_types=['text'])
# def answer(message):
#     if message.chat.type == 'private':


bot.polling(none_stop=True)