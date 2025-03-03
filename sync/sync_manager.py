from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from sync import CONFIG
from utils import helpers

class CloudSync:
    def __init__(self, credentials_path=CONFIG.CREDENTIAL_PATH):
        """ Inicializa la autenticación con Google Drive usando un archivo JSON """
        self.auth = GoogleAuth()
        self.auth.LoadClientConfigFile(credentials_path)  # Carga el JSON de credenciales

        # Intenta cargar credenciales previamente guardadas
        if not self.auth.LoadCredentialsFile("credentials.json"):
            self.auth.LocalWebserverAuth()  # Abre el navegador solo si es necesario
            self.auth.SaveCredentialsFile("credentials.json")  # Guarda las credenciales

        self.drive = GoogleDrive(self.auth)

        # Verificar si la autenticación fue exitosa
        if self.auth.credentials is None or self.auth.access_token_expired:
            print("Autentication Failed.")
        else:
            print("Autentication completed.")

    def sync_files(self):
        """ Sync files betwen local files and cloud files. """
        self.local_sync.get_files()
        self.cloud_sync.get_files()
 
    def get_auth(self):
        """Devuelve la autenticación para que otros módulos la usen"""
        return self.auth

    def run(self):
        """ Ejecuta la sincronización. """
        # self.logger.info("Iniciando sincronización...")
        self.sync_files()
        # self.logger.info("Sincronización finalizada.")