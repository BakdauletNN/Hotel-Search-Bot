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
        send_info(message, photos=0)
    else:
        bot.send_message(message.chat.id, 'Введите "да" или "нет".')