from loader import bot
import handlers
from utils.set_bot_commands import set_default_commands


if __name__ == '__main__':
    set_default_commands(bot)
    bot.infinity_polling()


# def test():
#     a = input('Enter ages with commas: ')
#     ages = [int(age.strip()) for age in a.split(',') if age.strip().isdigit()]
#     if ages:
#         for age in ages:
#             print(age, end=' ')
#             print(type(age), end=' ')
#     else:
#         print('Error')
#
# test()
#
#

