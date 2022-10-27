import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

DB_URL = os.environ.get("DB_URL","")
DB_NAME = os.environ.get("DB_NAME","")
DB_USER = os.environ.get("DB_USER","")
DB_PASS = os.environ.get("DB_PASS","")
DB_PORT = os.environ.get("DB_PORT","")