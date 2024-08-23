from loader import bot
from states.contact_information import UserInfoState
from telebot.types import Message
from utils.send_info_hotel import send_info


@bot.message_handler(state=UserInfoState.quantity_photo)
def photos_hotel(message: Message):
    if message.text.lower() == 'да':
        bot.set_state(message.from_user.id, UserInfoState.final, message.chat.id)
        bot.send_message(message.chat.id, 'Введите количество фотографий для каждого отеля (не больше 5)')
    elif message.text.lower() == 'нет':
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['photos'] = 0
        if data.get('command') == 'bestdeal':
            bot.send_message(message.chat.id, 'Введите минимальную стоимость в долларах')
            bot.set_state(message.from_user.id, UserInfoState.price_min, message.chat.id)
            return
        else:
            bot.send_message(message.chat.id, 'Вот вам отели')
            answer = send_info(data)
            for item in answer:
                if isinstance(item, tuple) and item[0] == 'photo':
                    bot.send_photo(message.chat.id, item[1])
                else:
                    bot.send_message(message.chat.id, item)
        bot.delete_state(message.from_user.id, message.chat.id)
    else:
        bot.send_message(message.chat.id, 'Введите "да" или "нет".')
