from flask import Flask, request, jsonify
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")  # важно для CodePen/внешних клиентов

@app.route("/send", methods=["POST"])
def send():
    data = request.get_json()
    username = data.get("username", "Anonymous")
    lottie_url = data.get("lottieUrl", "")

    gift = {
        "username": username,
        "lottieUrl": lottie_url
    }

    socketio.emit("gift", gift)
    return jsonify({"status": "ok", "gift": gift})

@app.route("/")
def index():
    return "myalerts Lottie server is running"

if __name__ == "__main__":
    # Локальный запуск
    socketio.run(app, host="0.0.0.0", port=5000)
