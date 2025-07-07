from flask import request, jsonify, render_template
from app.webhook.utils import extract_author, extract_from_branch, extract_to_branch
from app.extensions import mongo
from datetime import datetime, timezone
from app import create_app

app = create_app()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/events')
def get_events():
    try:
        print("Mongo client address:", mongo.cx.address if hasattr(mongo.cx, "address") else "No address")
        events = list(mongo.db.webhook_logs.find().sort("timestamp", -1).limit(10))
        return jsonify(events)
    except Exception as e:
        print("Error fetching events:", e)
        return jsonify({"error": "Could not fetch events"}), 500
##--------------------
@app.route("/test-db")
def test_db():
    try:
        mongo.db.webhook_logs.insert_one({"msg": "Hello, MongoDB!"})
        return "Insert successful"
    except Exception as e:
        return f"Insert failed: {e}"
#-------------------- 

@app.route('/webhook/receiver', methods=['POST'])
def webhook_receiver():
    data = request.json
    event_type = request.headers.get('X-GitHub-Event')

    # Process only push and pull_request
    if event_type in ["push", "pull_request"]:
        record = {
            "event_type": event_type,
            "author": extract_author(data, event_type),
            "from_branch": extract_from_branch(data, event_type),
            "to_branch": extract_to_branch(data, event_type),
            "timestamp": datetime.now(timezone.utc).isoformat()
        }

        # Insert into MongoDB
        try:
            mongo.db.webhook_logs.insert_one(record)
            return jsonify({"status": "logged"}), 201
        except Exception as e:
            print(f"MongoDB insertion error: {e}")
            return jsonify({"error": "failed to log to database"}), 500

    return jsonify({"error": "Unsupported event type"}), 400

if __name__ == '__main__':
    app.run(debug=True)