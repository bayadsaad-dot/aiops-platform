import time

from collector import collect_metrics
from collectors.network_collector import collect_network_metrics
from collectors.process_collector import collect_processes
from api.process_api import send_processes
from senders.metrics import send_metrics
from senders.network import send_network
from senders.heartbeat import send_heartbeat


def main():
    print("🚀 Monitoring Agent Started...")

    while True:

        # System metrics
        metrics = collect_metrics()
        send_metrics(metrics)

        # Heartbeat
        send_heartbeat(metrics["hostname"])

        # Network
        network = collect_network_metrics()
        send_network(network)

        # Processes
        processes = collect_processes()
        send_processes(
            backend_url="http://127.0.0.1:8000",
            hostname=metrics["hostname"],
            processes=processes,
        )

        time.sleep(2)


if __name__ == "__main__":
    main()