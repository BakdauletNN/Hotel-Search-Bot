Telegram Bot for Hotel Search

Project Structure

Root Files

.env.template: Template for environment variables. After cloning the repository, remove the .template suffix and enter your token and API key.

loader.py: Provides the bot's basic infrastructure, including logging, user state management, and other essential functions.

requirements.txt: Contains a list of dependencies required for the Telegram bot to run.

debug.log: Log file storing the bot's operational history.

main.py: Starts the bot and initializes the database.

Folders and Files

config_data


config.py: Insert your API key and token here. Also, define the bot's command set.

database

models.py: Manages database operations using the Peewee ORM library.

get_history.py: Retrieves the user's history from the database based on their ID.

tg_bot.db: Database file for storing user data and other bot-related information.

handlers

default_handlers:


start.py: Handles the welcome message.

help.py: Displays a list of available commands.

echo.py: Echoes any message that does not match a command.

custom_handlers (All custom handlers):


init.py: Manages the execution order of handlers.

command_handler.py: Defines commands, creates data objects, and obtains the user’s location.

callback_data.py: Manages user selections via inline buttons.

adults.py: Handles the number of adults for the search.

children.py: Manages the number of children and their ages.

entry_date.py: Validates the age data for children.

exit_date.py: Manages the check-in date.

check_hotels_amount.py: Manages the check-out date.

quantity_hotels.py: Specifies the number of hotels to find.

photos_amount.py: Manages the requested number of photos. If no photos are required, results are provided immediately.

send_info_hotel.py: Sends search results and saves data to the database.

result.py: Sends search results with photos.



min_price_bestdeal.py: Specifies the minimum price for finding the best deals.

max_price_bestdeal.py: Specifies the maximum price for finding the best deals.

distance_bestdeal.py: Specifies the distance from the city center and sends hotel search results.

history.py: Manages database operations related to the user’s search history.

keyboards

keyboards.py: Implements inline buttons for user interaction.

states

contact_information.py: Manages states for interacting with the user.

utils

get_city_user.py: Parses city data from RapidAPI based on user input.

hotels_params.py: Transfers user-entered data and parses hotel information, including ID, name, and nightly rate.

hotel_information.py: Retrieves hotel information, such as links, photos, and location.

set_bot_commands.py: Defines commands for the bot.