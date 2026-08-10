import psutil


def collect_processes():

    processes = []

    for proc in psutil.process_iter(
        [
            "pid",
            "name",
            "username",
            "exe",
            "cpu_percent",
            "memory_percent",
        ]
    ):

        try:

            info = proc.info

            processes.append(
                {
                    "pid": info["pid"],
                    "name": info["name"] or "",
                    "cpu_percent": info["cpu_percent"] or 0,
                    "memory_percent": round(
                        info["memory_percent"] or 0,
                        2,
                    ),
                    "executable": info["exe"],
                    "username": info["username"],
                    "is_running": True,
                }
            )

        except (
            psutil.NoSuchProcess,
            psutil.AccessDenied,
            psutil.ZombieProcess,
        ):
            continue

    return processes