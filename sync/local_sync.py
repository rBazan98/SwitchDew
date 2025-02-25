import os
from sync import CONFIG
import shutil

class LocalSync:
    def __init__(self, local_path):
        self.local_path = local_path

    def get_files(self):
        """ Get files from steam folder """
        if CONFIG["SYSTEM_OS"] == "Linux":
            # src = "/home/$USER/.config/StardewValley/Saves/Hello_396429681"
            src = os.path.expandvars("/home/$USER/.config/StardewValley/Saves/Hello_396429681")
            dst = CONFIG["LOCAL_PATH"]
            shutil.rmtree(dst, ignore_errors=True)
            shutil.copytree(src, dst, dirs_exist_ok=True)
        elif CONFIG["SYSTEM_OS"] == "Windows":
            pass
        else:
            pass


    def list_files(self):
        """ Devuelve una lista de archivos en la carpeta local. """
        pass


    def file_exists(self, filename):
        """ Verifica si un archivo existe en la carpeta local. """
        pass


    def delete_file(self, filename):
        """ Elimina un archivo de la carpeta local. """
        pass