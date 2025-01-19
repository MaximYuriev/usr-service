from .config import RMQ_PASS, RMQ_USER, RMQ_HOST

rabbit_url = f"amqp://{RMQ_USER}:{RMQ_PASS}@{RMQ_HOST}:5672/"