# __init__.py

import certifi
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
    mongo.init_app(app, tlsCAFile=certifi.where(), tlsAllowInvalidCertificates=True)
    if not app.config["MONGO_URI"]:
        raise Exception("MONGO_URI is missing in environment variables")
    
    init_app(app)
    
    # registering all the blueprints
    app.register_blueprint(webhook)
    
    return app
