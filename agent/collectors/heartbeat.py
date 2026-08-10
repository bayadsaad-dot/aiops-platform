from datetime import datetime, timezone


def collect_heartbeat():
    return datetime.now(timezone.utc).isoformat()