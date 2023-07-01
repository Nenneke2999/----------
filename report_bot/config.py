from dotenv import load_dotenv
import os
load_dotenv()
BOT_TOKEN = os.environ.get('BOT_TOKEN')
USER = os.environ.get('USER')
PASSWORD = os.environ.get('PASSWORD')
DATABASE = os.environ.get('DATABASE')
PORT = os.environ.get('PORT')
HOST = os.environ.get('HOST')