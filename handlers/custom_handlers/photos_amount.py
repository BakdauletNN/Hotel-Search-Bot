from loader import bot
from states.contact_information import UserInfoState
from telebot.types import Message
from handlers.custom_handlers.send_info_hotel import send_info


@bot.message_handler(state=UserInfoState.quantity_photo)
def photos_hotel(message: Message):
    if message.text.lower() == 'да':
        bot.set_state(message.from_user.id, UserInfoState.final, message.chat.id)
        bot.send_message(message.chat.id, 'Кол-во фоток для каждого отеля, не больше 5')
    elif message.text.lower() == 'нет':
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['photos'] = 0
        bot.set_state(message.from_user.id, UserInfoState.final, message.chat.id)
        send_info(message)  # Вызов функции отправки информации сразу
    else:
        bot.send_message(message.chat.id, 'Введите "да" или "нет".')
