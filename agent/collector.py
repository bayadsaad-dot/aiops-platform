import psutil
from datetime import datetime

from collectors.cpu import collect_cpu
from collectors.memory import collect_memory
from collectors.disk import collect_disk


def collect_metrics():
    return {
        "hostname": "blanco",
        "ip_address": "10.10.3.128",
        "cpu_usage": collect_cpu(),
        "memory_usage": collect_memory(),
        "disk_usage": collect_disk(),
        "uptime_seconds": int(datetime.now().timestamp() - psutil.boot_time()),
        "boot_time": datetime.fromtimestamp(psutil.boot_time()).isoformat(),
    }