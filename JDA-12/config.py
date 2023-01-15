from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env

basedir = os.path.abspath(os.path.dirname(__file__))


APP_NAME = "Jobs Data Analyzer"
FLASK_ADMIN_SWATCH = 'cerulean'
TEMPLATES_AUTO_RELOAD = False

SQLALCHEMY_LOCAL_DATABASE_URI = os.getenv('PG_LOCAL_URI')
SQLALCHEMY_REMOTE_DATABASE_URI = os.getenv('PG_REMOTE_URI')
SQLALCHEMY_TRACK_MODIFICATIONS = False

WTF_CSRF_ENABLED = True
SECRET_KEY = "SECRET"