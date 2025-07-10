# app/webhook/routes.py

from flask import Blueprint


# Define the blueprint for the webhook routes
webhook = Blueprint('Webhook', __name__, url_prefix='/api/events')