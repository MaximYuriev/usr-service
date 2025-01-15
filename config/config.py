import os

from dotenv import load_dotenv

load_dotenv()

POSTGRES_DB = os.environ.get("POSTGRES_DB")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
POSTGRES_PORT = os.environ.get("POSTGRES_PORT")
POSTGRES_HOST = os.environ.get("POSTGRES_HOST")
POSTGRES_USER = os.environ.get("POSTGRES_USER")

RMQ_PASS = os.environ.get("RMQ_PASS")
RMQ_USER = os.environ.get("RMQ_USER")
