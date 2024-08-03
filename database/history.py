from loader import bot
from telebot.types import Message
from database.models import History


@bot.message_handler(commands=['history'])
def command_history(message: Message) -> None:
    try:
        history = History.select().where(History.user_id == message.from_user.id)
        if history.exists():
            response = "История запросов:\n"
            for record in history:
                response += f"{record.command} в {record.city} на {record.request_date.strftime('%Y-%m-%d')}\n"
            bot.send_message(message.chat.id, response)
        else:
            bot.send_message(message.chat.id, "История не найдена.")
    except Exception as e:
        bot.send_message(message.chat.id, "Произошла ошибка при получении истории, попробуйте позже.")
