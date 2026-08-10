import psutil


def collect_memory():
    return psutil.virtual_memory().percent