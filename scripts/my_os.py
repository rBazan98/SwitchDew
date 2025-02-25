import os
import platform
from dotenv import load_dotenv

load_dotenv()  # Carga variables de entorno desde .env

CONFIG = {
    "SYSTEM_OS": os.getenv("SYSTEM_OS", platform.system()),
    "LOCAL_PATH": os.getenv("LOCAL_PATH", "./local_files"),
    "CLOUD_PATH": os.getenv("CLOUD_PATH", "./cloud_files"),
    # "CLOUD_FOLDER_ID": os.getenv("CLOUD_FOLDER_ID"),
    "LOG_FILE": os.getenv("LOG_FILE", "sync.log")
}