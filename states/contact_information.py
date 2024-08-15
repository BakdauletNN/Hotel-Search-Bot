from telebot.handler_backends import StatesGroup, State


class UserInfoState(StatesGroup):
    user_city = State()
    id_location = State()
    amount_adults = State()
    amount_child = State()
    age_child = State()
    date_entry = State()
    date_exit = State()
    get_hotels_amount = State()
    photo = State()
    quantity_photo = State()
    price_min = State()
    price_max = State()
    distance = State()
    final = State()

