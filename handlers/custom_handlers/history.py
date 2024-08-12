from loader import bot
from telebot.types import Message
from database.get_history import get_history_user


@bot.message_handler(commands=['history'])
def command_history(message: Message) -> None:
    bot.delete_state(message.from_user.id, message.chat.id)
    try:
        history = get_history_user(user_id_tg=message.from_user.id)
        if history.exists():
            response = "История запросов:\n"
            for record in history:
                response += f"\nКоманда: {record.command}" \
                            f"\nГород: {record.city}" \
                            f"\nДата запроса: {record.request_date.strftime('%Y-%m-%d')}" \
                            f"\nАйди локации: {record.location_id}" \
                            f"\nКол-во взрослых: {record.adults_qty}" \
                            f"\nКол-во детей: {record.children}" \
                            f"\nДата въезда: {record.entry_date}" \
                            f"\nДата выезда: {record.exit_date}" \
                            f"\nКол-во отелей: {record.hotels_quantity}" \
                            f"\nКол-во фоток: {record.photo_qty}" \
                            f"\nМин прайс: {record.min_price}" \
                            f"\nМакс прайс: {record.max_price}" \
                            f"\nРасстояние от центра: {record.distance_from_center} "
            bot.send_message(message.chat.id, response)
        else:
            bot.send_message(message.chat.id, "История не найдена.")
    except Exception as e:
        bot.send_message(message.chat.id, "Произошла ошибка при получении истории, попробуйте позже.")
