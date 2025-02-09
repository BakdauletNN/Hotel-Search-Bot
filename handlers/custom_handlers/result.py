from loader import bot
from states.contact_information import UserInfoState
from telebot.types import Message
from utils.send_info_hotel import send_info


@bot.message_handler(state=UserInfoState.final)
def finally_answer(message: Message):
    if not message.text.isdigit() or not 1 <= int(message.text) <= 5:
        bot.send_message(message.chat.id, 'Invalid input. Please enter a number from 1 to 5.')
        return

    photos = int(message.text)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data.update({'photos': photos})

        if data.get('command') == 'bestdeal':
            bot.send_message(message.chat.id, 'Enter the minimum value in dollars')
            bot.set_state(message.from_user.id, UserInfoState.price_min, message.chat.id)
            return

        bot.send_message(message.chat.id, 'Hotels -->')
        result_hotel = send_info(data)
        for item in result_hotel:
            if isinstance(item, tuple) and item[0] == 'photo':
                bot.send_photo(message.chat.id, item[1])
            else:
                bot.send_message(message.chat.id, item)

    bot.delete_state(message.from_user.id, message.chat.id)
