from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from sync import CONFIG
from utils import helpers

class CloudSync:
    def __init__(self):
        self.auth = GoogleAuth()
        # self.auth.LocalWebserverAuth()
        self.drive = GoogleDrive(self.auth)

    def get_files(self, filename):
        """ Get files from steam folder """
        if CONFIG.SYSTEM_OS == "Linux":
            pass
        elif CONFIG.SYSTEM_OS == "Windows":
            pass
        else:
            pass

    def list_files(self, folder_id):
        """ Devuelve una lista de archivos en la carpeta de Google Drive. """
        pass

    def upload_file(self, local_path, folder_id):
        """ Sube un archivo local a Google Drive. """
        pass

    def delete_file(self, file_id):
        """ Elimina un archivo de Google Drive. """
        pass