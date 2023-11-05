from telebot.handler_backends import StatesGroup, State


class UserInfoState(StatesGroup):
    user_city = State()
    city_list = State()
    callback_data = State()
