import os
import redis
from flask import Flask

app = Flask(__name__)

redis_host = os.environ.get("REDIS_HOST", "redis")
redis_port = os.environ.get("REDIS_PORT", 6379)
redis_password = os.environ.get("REDIS_PASSWORD", None)

r = redis.Redis(host=redis_host, port=redis_port, password=redis_password)

@app.route('/', methods=['GET'])
def hello():
    return "Hello, World!"

@app.route("/get/<key>", methods=['GET'])
def get_value(key):
    value = r.get(key)
    return value if value else "Key not found"

@app.route("/set/<key>/<value>", methods=['POST'])
def set_value(key, value):
    r.set(key,value)
    return f"Set {key} to {value}"

@app.route("/getall", methods=['GET'])
def get_all():
    keys = r.keys()
    values = [r.get(key) for key in keys]
    datab = zip(keys, values)
    s = ""
    for x in datab:
      s += f"{x[0].decode('ascii')}: {x[1].decode('ascii')} <br/>"
    return s

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)