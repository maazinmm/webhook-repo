import pymongo
from pymongo import MongoClient

uri = "mongodb+srv://webhook-user:webh00k@webhook-db.t947vf0.mongodb.net/webhook_db?retryWrites=true&w=majority&tls=true"

client = MongoClient(uri)

try:
    client.admin.command('ping')
    print("✅ Connected to MongoDB Atlas!")
except Exception as e:
    print(f"❌ Connection failed: {e}")
