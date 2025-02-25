import logging

def setup_logger(log_file="sync.log"):
    logger = logging.getLogger("SwitchDewLogger")
    logger.setLevel(logging.INFO)

    handler = logging.FileHandler(log_file)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    return logger