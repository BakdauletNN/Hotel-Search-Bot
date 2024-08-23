from database.models import History


def get_history_user(user_id_tg: int):
    return History.select().where(History.user_id == user_id_tg)

