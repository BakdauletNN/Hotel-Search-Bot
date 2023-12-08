from loader import bot
from states.contact_information import UserInfoState
from telebot.types import Message


@bot.message_handler(state=UserInfoState.hotel_photo)
def adults(message: Message) -> None:
    user = bot.send_message(message.chat.id, 'Нужны фотографии?')
    if user == 'да':

    #Дальнейшие действии и сохраняем весь процесс

    # bot.set_state(message.from_user.id, UserInfoState.hotel_photo, message.chat.id)
    #     with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
    #         data['hotel_photos'] = message.text
    elif user == 'нет':
        pass




