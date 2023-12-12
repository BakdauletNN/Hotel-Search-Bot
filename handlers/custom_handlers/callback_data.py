from loader import bot
import re
from states.contact_information import UserInfoState
from telebot.types import Message
from datetime import datetime,date


@bot.callback_query_handler(func=lambda call: call.data.startswith("callback_data:"))
def handle_location_callback(call):
    chosen_city = re.search(r'callback_data:(.*)', call.data).group(1) # Получение выбранного города из данных обратного вызова

    bot.set_state(call.from_user.id, UserInfoState.amount_adults, call.message.chat.id)
    with bot.retrieve_data(call.from_user.id, call.message.chat.id) as data:
        data['id_location'] = chosen_city
#     bot.send_message(call.from_user.id, "Введите кол-во взрослых:")
#
#
# @bot.message_handler(state=UserInfoState.amount_adults)
# def adults(message: Message) -> None:
#     if message.text.isdigit():
#         with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
#             data['adults'] = message.text
#         bot.send_message(message.chat.id, 'Имеется ли у вас дети? (да/нет)')
#     else:
#         bot.send_message(message.chat.id, 'Некорректный ввод')
#
#
# @bot.message_handler(state=UserInfoState.amount_child)
# def child(message: Message) -> None:
#     if message.text.lower() == 'да':
#         bot.send_message(message.chat.id, 'Кол-во детей')
#         with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
#             data['child_amount'] = message.text
#
#         bot.send_message(message.chat.id, 'Возраст детей')
#         bot.set_state(message.from_user.id, UserInfoState.age_child, message.chat.id)
#
#     else:
#         bot.send_message(message.chat.id, 'Хорошо, детей с собой нету')
#
#
# @bot.message_handler(state=UserInfoState.age_child)
# def age_children(message: Message) -> None:
#     if message.text.isdigit():
#         bot.send_message(message.chat.id, 'Возраст записан,Теперь введите дата '
#                                           'въезда в таком формате(01.04.2021')
#
#         bot.set_state(message.from_user.id, UserInfoState.date_entry, message.chat.id)
#
#         with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
#             data['child_age'] = message.text
#
#     else:
#         bot.send_message(message.chat.id, 'Возраст может быть только числом')
#
#
# @bot.message_handler(state=UserInfoState.date_entry)
# def entry_date(message: Message) -> None:
#     try:
#         entry_date = datetime.strptime(message.text, '%d.%m.%Y')
#
#         if entry_date.date() >= date.today():
#             with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
#                 data['entry'] = entry_date.strftime('%d.%m.%Y')
#
#             bot.send_message(message.chat.id, 'Хорошо, Введите дату выезда')
#             bot.set_state(message.from_user.id, UserInfoState.date_exit, message.chat.id)
#         else:
#             bot.send_message(message.chat.id, 'Введенная дата должна быть не ранее текущей даты. Попробуйте еще раз.')
#
#     except ValueError:
#         bot.send_message(message.chat.id, 'Некорректный формат даты. Введите дату в формате dd.mm.yyyy.')
#
#
#
# @bot.message_handler(state=UserInfoState.date_exit)
# def exit_date(message: Message) -> None:
#     try:
#         exit_date = datetime.strptime(message.text, '%d.%m.%Y')
#
#         if exit_date.date() >= date.today():
#             with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
#                 data['exit'] = exit_date.strftime('%d.%m.%Y')
#
#             bot.send_message(message.chat.id, 'Хорошо, введите количество отелей')
#             bot.set_state(message.from_user.id, UserInfoState.number_hotel, message.chat.id)
#         else:
#             bot.send_message(message.chat.id, 'Введенная дата должна быть не ранее текущей даты. Попробуйте еще раз.')
#
#     except ValueError:
#         bot.send_message(message.chat.id, 'Некорректный формат даты. Введите дату в формате dd.mm.yyyy.')
#
#
# @bot.message_handler(state=UserInfoState.number_hotel)
# def amount_hotel(message: Message) -> None:
#     if message.text.isdigit():
#         with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
#             data['hotels_number'] = message.text
#     else:
#         bot.send_message(message.chat.id, 'некорректный ввод')
#
#




