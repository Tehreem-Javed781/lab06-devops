import os
import random

from flask import Flask, jsonify, request

REGISTRATION_NUMBER = "FA23-BDS-041"

# Seed comes from docker-compose.yml (ROLL_SEED), so you can change it
# without rebuilding the image. Numeric values are used as int, else as string.
seed_raw = os.environ.get("ROLL_SEED", "41")
seed = int(seed_raw) if seed_raw.lstrip("-").isdigit() else seed_raw

# Fixed procedure from the lab handout (order matters)
random.seed(seed)
a1 = random.uniform(-5, 5)
a2 = random.uniform(-5, 5)
a3 = random.uniform(-5, 5)
b = random.uniform(-10, 10)

app = Flask(__name__)
app.json.sort_keys = False  # keep keys in the order shown in the handout


@app.route("/predict")
def predict():
    try:
        x1 = float(request.args["x1"])
        x2 = float(request.args["x2"])
        x3 = float(request.args["x3"])
    except (KeyError, ValueError):
        return jsonify({"error": "x1, x2 and x3 must be provided as numbers"}), 400

    y = a1 * x1 + a2 * x2 + a3 * x3 + b
    return jsonify({
        "registration number": REGISTRATION_NUMBER,
        "prediction": round(y, 2),
    })


@app.route("/")
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
