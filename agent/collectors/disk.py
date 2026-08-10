import psutil


def collect_disk():
    return psutil.disk_usage("/").percent