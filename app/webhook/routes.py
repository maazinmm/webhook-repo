# #app/webhook/routes.py

# from flask import Blueprint
# from flask_cors import CORS
# from app.extensions import mongo

# webhook = Blueprint('Webhook', __name__, url_prefix='/api/events')

# CORS(webhook)

# # Registering the webhook blueprint
# @webhook.route('/')
# def index():
#     return "Webhook API is running", 200
# @webhook.route('/test-db', methods=["GET"])
# def test_db():
#     mongo.db.webhook_logs.insert_one({"msg": "Hello, MongoDB!"})
#     return "Insert successful", 200
# @webhook.route('/events', methods=["GET"])
# def get_events():
#     events = list(mongo.db.webhook_logs.find().sort("timestamp", -1).limit(10))
#     return {"events": events}, 200

# @webhook.route('/receiver', methods=["POST"])
# def receiver():
#     return {}, 200
