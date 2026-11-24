import random
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "service": "dice-roller-api"})


@app.route("/roll", methods=["POST", "GET"])
def roll_dice():
    if request.method == "POST":
        data = request.get_json(silent=True) or {}
        num_dice = data.get("num_dice", 1)
        num_sides = data.get("num_sides", 6)
    else:
        num_dice = request.args.get("num_dice", default=1, type=int)
        num_sides = request.args.get("num_sides", default=6, type=int)

    try:
        num_dice = int(num_dice)
        num_sides = int(num_sides)
    except (TypeError, ValueError):
        return jsonify({"error": "num_dice and num_sides must be integers"}), 400

    if not (1 <= num_dice <= 100):
        return jsonify({"error": "num_dice must be between 1 and 100"}), 400
    if not (2 <= num_sides <= 1000):
        return jsonify({"error": "num_sides must be between 2 and 1000"}), 400

    rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
    return jsonify({
        "notation": f"{num_dice}d{num_sides}",
        "num_dice": num_dice,
        "num_sides": num_sides,
        "rolls": rolls,
        "total": sum(rolls),
        "min": min(rolls),
        "max": max(rolls),
    })


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5001)
