import os
from dotenv import load_dotenv, find_dotenv


if not find_dotenv():
    exit("Environment variables are not loaded because the .env file is missing")
else:
    load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
API_KEY = os.getenv("API_KEY")
DEFAULT_COMMANDS = (
    ("start", "Launch bot"),
    ("help", "Get help"),
    ("low", 'Minimum services'),
    ("high", 'Maximum services'),
    ("bestdeal", 'Your parameters'),
    ("history", 'History')
)
