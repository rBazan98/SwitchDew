import os

def get_savefile():
    pass

def send_savefile():
    pass

def compress_local_file():
    pass

def local_backup():
    pass

def switch_backup():
    pass

def hash_savefile():
    pass

def write_local():
    pass

def is_switch_file():
    pass

def is_steam_file():
    pass

def is_sync():
    pass

def run():
    local_file = './local/local.zip'
    cloud_file = './cloud/cloud.zip'

    local_file_old = './local/local.zip.old'
    cloud_file_old = './cloud/cloud.zip.old'

    log_file = 'logfile.log'

    if not os.path.exists(local_file):
        compress_local_file()
    local_save_time = get_local_time()

    if not os.path.exists(cloud_file):
        get_savefile()
        cloud_save_time = get_cloud_time()
        # rename cloud file

    assert os.path.exists(local_file) and os.path.exists(cloud_file)

    if hash_savefile(local_file) == hash_savefile(cloud_file):
        return

    if local_save_time > cloud_save_time:
        send_savefile()
    elif local_save_time < cloud_save_time:
        write_to_local()

if __name__ == '__main__':
    run()