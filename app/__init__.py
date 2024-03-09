from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate
# from dotenv import load_dotenv
import os
# from config import Config

# load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv("TRACK_MODIFICATIONS", False)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes
