# from dotenv import load_dotenv
# import os


# load_dotenv()

# CONFIG_MODE = os.environ.get("CONFIG_MODE", "testing")

# class LocalConfig(BaseConfig):
#     pass

# class TestingConfig():
#     MODE = CONFIG_MODE

#     # Exchange rates
#     COIN_API_URL = ""

#     # Logging
#     ENABLE_LOGGING = get_bool_variable("ENABLE_LOGGING", False)

#     # SQL
#     DATABASE_URL = "sqlite:///:memory:"

# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from orm.sql_models.base import Base

# engine = create_engine('sqlite:///site.db', echo=True)  # Adjust the connection string accordingly
# Session = sessionmaker(bind=engine)

import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

DATABASE = os.getenv('DATABASE')
DATABASE_USERNAME = os.getenv('DATABASE_USERNAME')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
# DATABASE_URL = os.getenv('DATABASE_URL')

# CONN = create_engine(DATABASE_URL)

class Config:
    # General Flask Config
    # DEBUG = os.environ.get('DEBUG', False)
    # SECRET_KEY = os.environ.get('SECRET_KEY', 'your_secret_key')

    # Database Config
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # SQLAlchemy Session Config
    ENGINE = create_engine(SQLALCHEMY_DATABASE_URI)
    Session = sessionmaker(bind=ENGINE)

    # Other Configurations
    # Add any other configuration variables you need for your application
