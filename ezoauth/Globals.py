import os
from dotenv import load_dotenv

load_dotenv()


def getenv(var_name: str):
    default_values = {
        "LOG_LEVEL": "INFO",
        "LOG_FORMAT": "%(asctime)s | %(levelname)s | %(message)s",
        "DEFAULT_USER": "user",
    }
    default_value = default_values[var_name] if var_name in default_values else ""
    return os.getenv(var_name, default_value)
