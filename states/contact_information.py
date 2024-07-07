from telebot.handler_backends import StatesGroup, State


class UserInfoState(StatesGroup):
    user_city = State()
    city_list = State()
    id_location = State()
    amount_adults = State()
    amount_child = State()
    age_child = State()
    date_entry = State()
    date_exit = State()
    answer_hotel = State()
    quantity_photo = State()
