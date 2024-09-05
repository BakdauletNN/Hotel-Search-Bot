from telebot.types import Message
from database.get_history import get_history_user


def command_history(message: Message):
    print(f"Запрос истории для пользователя {message.from_user.id}")
    history = get_history_user(user_id_tg=message.from_user.id)
    if history:
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
        print('Here responce to command history')
        return response
    else:
        print("История не найдена")
        return "История не найдена."
