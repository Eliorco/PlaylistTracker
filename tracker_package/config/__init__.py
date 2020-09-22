import os

class Config:
    SECRET_KEY = "AIzaSyBZtiCuZ0LUYfoe3RqCksfck0rhQBZnRwvho"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///tracker.db?check_same_thread=False'
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS', False)
