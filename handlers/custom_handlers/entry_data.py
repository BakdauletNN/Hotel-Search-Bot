from loader import bot
from states.contact_information import UserInfoState
from telebot.types import Message
from datetime import datetime,date


@bot.message_handler(state=UserInfoState.date_entry)
def entry_date(message: Message) -> None:
    """

    :param message:
    :return: None
    Здесь проверяем что возраст являеться числом. Дальше делим дату и сохраняем
    """
    if message.text.isdigit():
        bot.send_message(message.from_user.id, 'Возраст записан. Теперь введите дата '
                                               'въезда в таком формате (01.04.2021)')
        # try:
        entry_config = datetime.strptime(message.text, '%d.%m.%Y')
        bot.set_state(message.from_user.id, UserInfoState.date_exit, message.chat.id)
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['entry'] = entry_config.strftime('%d.%m.%Y')


        # except ValueError:
        #     bot.send_message(message.chat.id, 'Некорректный формат даты. Введите дату в формате dd.mm.yyyy.')
    else:
        bot.send_message(message.from_user.id, 'Возраст может быть только числом')