from flask import Blueprint, json, request
from app.extensions import mongo

webhook = Blueprint('Webhook', __name__, url_prefix='/webhook')

@webhook.route('/receiver', methods=["POST"])
def receiver():
    return {}, 200
