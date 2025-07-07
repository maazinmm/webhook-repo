import os
from flask import Flask
from .extensions import init_app
from dotenv import load_dotenv

from app.webhook.routes import webhook

# Creating the flask app
def create_app():

    load_dotenv()
    db_password = os.getenv("DB_PASSWORD")

    if not db_password:
        raise ValueError("DB_PASSWORD environment variable not set")
    
    app = Flask(__name__)
    #app.config["MONGO_URI"] = f"mongodb+srv://webhook-user:{db_password}@webhook-db.t947vf0.mongodb.net/webhook_db?retryWrites=true&w=majority"
    app.config["MONGO_URI"] = (
    f"mongodb+srv://webhook-user:{db_password}@webhook-db.t947vf0.mongodb.net/?retryWrites=true&w=majority&tlsAllowInvalidCertificates=true"
)

    if not app.config["MONGO_URI"]:
        print("MONGO_URI Not Connected")
    else:
        print("MONGO_URI Connected Successfully")

    init_app(app)
    
    # registering all the blueprints
    app.register_blueprint(webhook)
    
    return app
