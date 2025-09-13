import redis
import json
from app.config import REDIS_HOST, REDIS_PORT


USE_REDIS = False
try:
    r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0, decode_responses=True)
    r.ping()  # Test connection
    USE_REDIS = True
except Exception as e:
    print(f"Error connecting to Redis: {e}")
    r = None


# In-memory fallback storage
message_storage = {}

def get_redis_key(user_id: str):
    return f"chat:{user_id}"


def save_message(user_id: str, message: str, role: str = "user"):
    if USE_REDIS:
        key = get_redis_key(user_id)
        r.rpush(key, json.dumps({"role": role, "content": message}))
    else:
        if user_id not in message_storage:
            message_storage[user_id] = []
        message_storage[user_id].append({"role": role, "content": message})


def get_recent_messages(user_id: str, limit: int = 10):
    if USE_REDIS:
        key = get_redis_key(user_id)
        messages = r.lrange(key, -limit, -1)
        return [json.loads(message) for message in messages]
    else:
        if user_id not in message_storage:
            message_storage[user_id] = []
        return message_storage[user_id][-limit:]


def clear_messages(user_id: str):
    key = get_redis_key(user_id)
    r.delete(key)
