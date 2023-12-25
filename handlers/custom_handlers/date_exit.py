from loader import bot
from states.contact_information import UserInfoState
from telebot.types import Message
from datetime import datetime,date


@bot.message_handler(state=UserInfoState.date_exit)
def exit_date(message: Message) -> None:
    """

    :param message:
    :return: None
    Делим дату въезда на день,месяц,год и сравниваем с сегодняшней датой
    """
    entry_config = datetime.strptime(message.text, '%d.%m.%Y')
    if entry_config.date() >= date.today():
        bot.send_message(message.chat.id, 'Дата въезда записана, введите дата выезда')
        # try:
        """
        
        Тут тоже делим и сохраняем через контекстный менеджер
        """
        exit_config = datetime.strptime(message.text, '%d.%m.%Y')

        bot.set_state(message.from_user.id, UserInfoState.answer_hotel, message.chat.id)
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['exit'] = exit_config.strftime('%d.%m.%Y')
        # except ValueError:
        #     bot.send_message(message.chat.id, 'Некорректный формат даты. Введите дату в формате dd.mm.yyyy.')

    else:
        bot.send_message(message.chat.id, 'Введенная дата должна быть не ранее текущей даты. Попробуйте еще раз.')


