from flask import Flask, request, jsonify
from flask_socketio import SocketIO

app = Flask(__name__)
# cors_allowed_origins="*" чтобы CodePen / внешний клиент мог подключаться
socketio = SocketIO(app, cors_allowed_origins="*")

# POST endpoint для отправки подарка
@app.route("/send", methods=["POST"])
def send():
    data = request.get_json()
    username = data.get("username", "Anonymous")
    lottie_url = data.get("lottieUrl", "")

    gift = {
        "username": username,
        "lottieUrl": lottie_url
    }

    # эмитим событие 'gift'
    socketio.emit("gift", gift)
    return jsonify({"status": "ok", "gift": gift})

@app.route("/")
def index():
    return "myalerts Lottie server is running"

if __name__ == "__main__":
    # host=0.0.0.0 для доступности с внешнего мира
    socketio.run(app, host="0.0.0.0", port=5000)
