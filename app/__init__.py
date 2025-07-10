# __init__.py

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from flask import Flask
from .extensions import init_app
from app.webhook.routes import webhook
import os
from dotenv import load_dotenv
load_dotenv()

# Creating flask app
def create_app():
    app = Flask(__name__)
    
    app.config["MONGO_URI"] = os.getenv("MONGO_URI")

    # Create new client and connect to database server
    client = MongoClient(app.config["MONGO_URI"], server_api=ServerApi('1'))

    # Test databse connection
    try:
        client.admin.command('ping')
        print("Pinged deployment. Successfully connected to MongoDB!")
    except Exception as e:
        print(e)
    
    # Register Blueprints
    app.register_blueprint(webhook)
    
    init_app(app)
    return app
