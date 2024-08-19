from loader import bot
from states.contact_information import UserInfoState
from telebot.types import Message
from utils.send_info_hotel import send_info


@bot.message_handler(state=UserInfoState.final)
def finally_answer(message: Message):
    result_to_user = send_info(message)
    if result_to_user:
        bot.send_message(message.chat.id, result_to_user)