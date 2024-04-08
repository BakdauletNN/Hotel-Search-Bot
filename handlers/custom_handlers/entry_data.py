from loader import bot
from states.contact_information import UserInfoState
from telebot.types import Message


@bot.message_handler(state=UserInfoState.date_entry)
def entry_date(message: Message) -> None:
    if [age for age in message.text.split(',') if age.strip().isdigit()]:
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['child_age'] =  ' '.join(message.text.split(','))
        bot.send_message(message.chat.id, f"ages:{message.text}")
        bot.set_state(message.from_user.id, UserInfoState.date_exit, message.chat.id)
        bot.send_message(message.chat.id, 'Теперь введите дату въезда в формате (01.04.2021)')
    else:
        bot.send_message(message.chat.id, 'Пожалуйста, введите возрасты детей через запятую.')
    if not [age.strip() for age in message.text.split(',') if age.strip().isdigit()]:
        bot.send_message(message.chat.id, 'Некорректные возрасты детей. Возраст должен быть числом.')





