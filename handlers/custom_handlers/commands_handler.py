from keyboards.keyboards import get_locations
from loader import bot
from states.contact_information import UserInfoState
from telebot.types import Message
from utils.low_price import city_info as low_city_info
from utils.high_price import city_info_user as high_city_info
from utils.bestdeal_city import city_info_bestdeal
from database import database


@bot.message_handler(commands=['low', 'high', 'bestdeal', 'history'])
def commands(message: Message) -> None:
    command = message.text.strip('/')
    bot.delete_state(message.from_user.id, message.chat.id)
    bot.set_state(message.from_user.id, UserInfoState.user_city, message.chat.id)

    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data.update({
            'command': command,
            'entry': None,
            'exit': None,
            'adults': None,
            'child_age': [],
            'id_location': None,
            'hotels_qty': None,
            'photos': None,
            'price_min_bestdeal': None,
            'price_max_bestdeal': None,
            'center_distance': None,
        })

    if command == 'history':
        history = database.get_history(message.from_user.id)
        if not history:
            bot.send_message(message.chat.id, 'История запросов пуста.')
        else:
            history_message = "История запросов:\n\n"
            for record in history:
                history_message += (
                    f"Команда: {record[1]}\n"
                    f"Город: {record[2]}\n"
                    f"Дата заезда: {record[3]}\n"
                    f"Дата выезда: {record[4]}\n"
                    f"Взрослых: {record[5]}\n"
                    f"Детей: {record[6]}\n"
                    f"ID Локации: {record[7]}\n"
                    f"Количество отелей: {record[8]}\n"
                    f"Фото: {record[9]}\n"
                    f"Мин. цена: {record[10]}\n"
                    f"Макс. цена: {record[11]}\n"
                    f"Расстояние от центра: {record[12]} миль\n"
                    f"Дата запроса: {record[13]}\n\n"
                )
            bot.send_message(message.chat.id, history_message)
    else:
        bot.send_message(message.chat.id, 'Введите город')


@bot.message_handler(state=UserInfoState.user_city)
def get_user_city(message: Message) -> None:
    if message.text.isalpha():
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['city'] = message.text  # Сохраняем город в данные пользователя
            command = data.get('command')
            if command == 'low':
                locations = low_city_info(message.text)
            elif command == 'high':
                locations = high_city_info(message.text)
            elif command == 'bestdeal':
                locations = city_info_bestdeal(message.text)
            else:
                bot.send_message(message.chat.id, 'Некорректная команда')
                return
        markup = get_locations(locations)
        bot.send_message(message.chat.id, 'Выберите локацию из списка:', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Некорректный ввод')

