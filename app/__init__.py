from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap

my_app = Flask(__name__)
my_app.config.from_object(Config)

from app import routes

boostrap = Bootstrap(my_app)
