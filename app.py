from flask import Flask, request, jsonify
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route("/donate", methods=["POST"])
def donate():
    data = request.get_json()
    username = data.get("username", "Anonymous")
    amount = data.get("amount", 0)
    message = data.get("message", "")

    donation = {
        "username": username,
        "amount": amount,
        "message": message
    }

    socketio.emit("donation", donation)
    return jsonify({"status": "ok", "donation": donation})

@app.route("/")
def index():
    return "myalerts is running"

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)
