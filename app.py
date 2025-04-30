from flask import Flask, request
import redis
from utils import get_secret

app = Flask(__name__)

redis_secret = get_secret("my-redis-secret")
r = redis.Redis(
    host=redis_secret["host"],
    port=redis_secret["port"],
    password=redis_secret.get("password"),
    decode_responses=True
)

@app.route("/latest")
def get_latest():
    name = r.get("latest_name")
    return f"Latest name: {name}" if name else "No name cached yet."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
