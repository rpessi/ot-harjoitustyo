import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass

CSV_FILENAME = os.getenv("CSV_FILENAME")
ACCOUNTS_FILENAME = os.getenv("ACCOUNTS_FILENAME")
JSON_PATH = os.getenv("JSON_PATH")
CSV_CONVERTED = os.getenv("CSV_CONVERTED")
