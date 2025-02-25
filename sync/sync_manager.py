from sync import LocalSync
from sync import CloudSync
from sync import CONFIG
from utils import setup_logger
import os

class SwitchDew:
    def __init__(self):
        self.local_sync = LocalSync(CONFIG["LOCAL_PATH"])
        self.cloud_sync = CloudSync()
        self.logger = setup_logger(CONFIG["LOG_FILE"])

    def sync_files(self):
        """ Sincroniza los archivos entre local y la nube. """
        self.local_sync.get_files()        

    def run(self):
        """ Ejecuta la sincronización. """
        self.logger.info("Iniciando sincronización...")
        self.sync_files()
        self.logger.info("Sincronización finalizada.")