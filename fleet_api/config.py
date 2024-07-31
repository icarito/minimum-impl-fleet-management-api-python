from os import environ
from dotenv import load_dotenv, dotenv_values

class Config:
    def __init__(self):
        load_dotenv()
        # setup non secret config variables here
        self.DATABASE_URL = environ.get('DATABASE_URL')
