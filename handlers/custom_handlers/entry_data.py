from loader import bot
from states.contact_information import UserInfoState
from telebot.types import Message
import re


@bot.message_handler(state=UserInfoState.date_entry)
def entry_date(message: Message) -> None:
    # Убедимся, что пользователь ввел возраст с пробелами
    if re.match(r'^[\d\s]+$', message.text):
        # Если да то сохраняем данные
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['child_age'] = message.text
        # Дальше заменяем состояние и просим дату въезда
        bot.set_state(message.from_user.id, UserInfoState.date_exit, message.chat.id)
        bot.send_message(message.chat.id, 'Теперь введите дату въезда в формате (01.04.2021)')
    else:
        bot.send_message(message.chat.id, 'Некорректный ввод')




