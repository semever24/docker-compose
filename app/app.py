# app/app.py
import os
from flask import Flask, jsonify, request, render_template
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps

MONGO_URI = os.environ.get("MONGO_URI", "mongodb://admin:password@mongo:27017")
MONGO_DB = os.environ.get("MONGO_DB", "mydb")
MONGO_COLLECTION = os.environ.get("MONGO_COLLECTION", "items")

app = Flask(__name__, template_folder="templates")

# Create a Mongo client on first request (lazy)
client = None
def get_collection():
    global client
    if client is None:
        client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
    db = client[MONGO_DB]
    return db[MONGO_COLLECTION]

@app.route("/")
def index():
    # The index page will fetch via the API (AJAX)
    return render_template("index.html")

@app.route("/api/items", methods=["GET"])
def get_items():
    col = get_collection()
    docs = list(col.find({}, {"_id": 1, "id": 1, "name": 1, "designation": 1, "city": 1}))
    # Use dumps to convert ObjectId properly
    return app.response_class(dumps(docs), mimetype="application/json")

@app.route("/api/items", methods=["POST"])
def add_item():
    payload = request.get_json(force=True)
    required = ["id", "name", "designation", "city"]
    if not all(k in payload for k in required):
        return jsonify({"ok": False, "error": "missing fields"}), 400
    col = get_collection()
    res = col.insert_one({
        "id": payload["id"],
        "name": payload["name"],
        "designation": payload["designation"],
        "city": payload["city"]
    })
    return jsonify({"ok": True, "inserted_id": str(res.inserted_id)}), 201

@app.route("/health")
def health():
    try:
        # quick server ping
        coll = get_collection()
        coll.database.command("ping")
        return jsonify({"status": "ok"})
    except Exception as e:
        return jsonify({"status": "error", "detail": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("FLASK_RUN_PORT", 5000)))