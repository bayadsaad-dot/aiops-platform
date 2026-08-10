import psutil


def collect_cpu():
    return psutil.cpu_percent(interval=1)