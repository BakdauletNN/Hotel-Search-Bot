from telebot.types import Message
from database.get_history import get_history_user


def command_history(message: Message):
    history = get_history_user(user_id_tg=message.from_user.id)
    if history:
        response = "Query history:\n"
        for record in history:
            response += f"\nCommand: {record.command}" \
                        f"\nCity: {record.city}" \
                        f"\nDate request: {record.request_date.strftime('%Y-%m-%d')}" \
                        f"\nId Location: {record.location_id}" \
                        f"\nQty adults: {record.adults_qty}" \
                        f"\nQty child: {record.children}" \
                        f"\nEntry date: {record.entry_date}" \
                        f"\nDeparture date: {record.exit_date}" \
                        f"\nNumber of hotels: {record.hotels_quantity}" \
                        f"\nNumber of photos: {record.photo_qty}" \
                        f"\nMin price: {record.min_price}" \
                        f"\nMax price: {record.max_price}" \
                        f"\nDistance from center: {record.distance_from_center} "
        return response
    else:
        return "History not found."
