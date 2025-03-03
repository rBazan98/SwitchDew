import os
import platform
from dotenv import load_dotenv

load_dotenv()  # Carga variables de entorno desde .env

CONFIG = {
    "SYSTEM_OS": os.getenv("SYSTEM_OS", platform.system()),
    "LOCAL_PATH": os.getenv("LOCAL_PATH", "./local_files"),
    "CLOUD_PATH": os.getenv("CLOUD_PATH", "./cloud_files"),
    "CLOUD_FOLDER_ID": os.getenv("FOLDER_ID", "1h1wK_2y2juNA59HPwj4HX-hlguk7tYV5"),
    "CREDENTIAL_PATH": os.getenv("CREDENTIAL_PATH", "./credentials/client_secret_339645879036-qub018k9frrt6nf51vu9a2kmvbn93end.apps.googleusercontent.com.json"),
    # "CLOUD_FOLDER_ID": os.getenv("CLOUD_FOLDER_ID"), #Config Drive
    "LOG_FILE": os.getenv("LOG_FILE", "sync.log")

}