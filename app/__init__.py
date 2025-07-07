# __init__.py

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from app.extensions import mongo
from flask import Flask
from .extensions import init_app
import os
from dotenv import load_dotenv
load_dotenv()


from app.webhook.routes import webhook

# Creating the flask app
def create_app():
    app = Flask(__name__)
    
    app.config["MONGO_URI"] = os.getenv("MONGO_URI")
    # Create a new client and connect to the server
    client = MongoClient(app.config["MONGO_URI"], server_api=ServerApi('1'))

    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

    init_app(app)
    
    # registering all the blueprints
    app.register_blueprint(webhook)
    
    return app
