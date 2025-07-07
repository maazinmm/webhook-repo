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
    if not app.config["MONGO_URI"]:
        raise Exception("MONGO_URI is missing in environment variables")
    
    db_password = os.getenv("DB_PASSWORD")
    if not db_password:
        raise ValueError("DB_PASSWORD environment variable not set")
    
    # Test connection to MongoDB
    if not app.config["MONGO_URI"]:
        print("MONGO_URI Not Connected")
    else:
        print("MONGO_URI Connected Successfully")

    init_app(app)
    
    # registering all the blueprints
    app.register_blueprint(webhook)
    
    return app
