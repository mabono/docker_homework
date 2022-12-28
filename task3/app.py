import os
import redis
from flask import Flask

app = Flask(__name__)

redis_host = os.environ.get("REDIS_HOST", "redis")
redis_port = os.environ.get("REDIS_PORT", 6379)
redis_password = os.environ.get("REDIS_PASSWORD", None)

r = redis.Redis(host=redis_host, port=redis_port, password=redis_password)

@app.route('/')
def hello():
    return "Hello, World!"

@app.route("/get/<key>")
def get_value(key):
    value = r.get(key)
    return value if value else "Key not found"

@app.route("/set/<key>/<value>")
def set_value(key, value):
    r.set(key,value)
    return f"Set {key} to {value}"
 
# @app.route("/all")
# def get_all():
#     if not r.keys():
#         return {} 
#     else:
#         keys = r.keys()
#         db_list = []
#         for key in keys:
#             db_list.append(f"{key.decode('ascii')}: {r.get(key).decode('ascii')}")
#         return f"{db_list}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)