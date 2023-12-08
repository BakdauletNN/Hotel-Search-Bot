from loader import bot
import re
from states.contact_information import UserInfoState


@bot.callback_query_handler(func=lambda call: call.data.startswith("callback_data:"))
def handle_location_callback(call):
    chosen_city = re.search(r'callback_data:(.*)', call.data).group(1) # Получение выбранного города из данных обратного вызова

    @bot.message_handler(state=UserInfoState.id_location)
    def save_id(message):
        bot.set_state(message.from_user.id, UserInfoState.id_location, message.chat.id)
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['id_location'] = chosen_city



    # Вызываем функцию save_id для обработки сообщения
    save_id(call.message)
