from loader import bot
import re
from states.contact_information import UserInfoState


@bot.callback_query_handler(func=lambda call: call.data.startswith("callback_data:"))
def handle_location_callback(call):
    chosen_city = re.search(r'callback_data:(.*)', call.data).group(
        1)  # Получаем выбранный город из данных обратного вызова

    bot.set_state(call.from_user.id, UserInfoState.amount_adults, call.message.chat.id)
    with bot.retrieve_data(call.from_user.id, call.message.chat.id) as data:
        data['id_location'] = chosen_city

    bot.send_message(call.from_user.id, "Введите кол-во взрослых:")

