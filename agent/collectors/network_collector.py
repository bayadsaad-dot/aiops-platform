from utils.network_speed import NetworkSpeedCalculator
import socket
import psutil

speed_calculator = NetworkSpeedCalculator()


def collect_network_metrics():

    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    stats = psutil.net_if_stats()
    addresses = psutil.net_if_addrs()
    counters = psutil.net_io_counters(pernic=True)

    interfaces = []

    for name, stat in stats.items():

        ipv4 = None
        mac = None

        if name in addresses:
            for addr in addresses[name]:

                if addr.family == socket.AF_INET:
                    ipv4 = addr.address

                elif getattr(psutil, "AF_LINK", None) == addr.family:
                    mac = addr.address

        lower = name.lower()

        if "wifi" in lower or "wi-fi" in lower or "wireless" in lower:
            interface_type = "Wi-Fi"

        elif "ethernet" in lower:
            interface_type = "Ethernet"

        elif "bluetooth" in lower:
            interface_type = "Bluetooth"

        elif "vmware" in lower or "vethernet" in lower:
            interface_type = "Virtual"

        elif "loopback" in lower:
            interface_type = "Loopback"

        else:
            interface_type = "Unknown"

        counter = counters.get(name)

        if counter:
            bytes_sent = counter.bytes_sent
            bytes_received = counter.bytes_recv
            packets_sent = counter.packets_sent
            packets_received = counter.packets_recv

            upload_speed, download_speed = (
                speed_calculator.calculate(
                    interface_name=name,
                    bytes_sent=bytes_sent,
                    bytes_received=bytes_received,
                )
            )

        else:
            bytes_sent = 0
            bytes_received = 0
            packets_sent = 0
            packets_received = 0
            upload_speed = 0.0
            download_speed = 0.0

        interfaces.append(
            {
                "name": name,
                "type": interface_type,
                "ipv4_address": ipv4,
                "mac_address": mac,
                "is_up": stat.isup,
                "speed": stat.speed,
                "mtu": stat.mtu,
                "bytes_sent": bytes_sent,
                "bytes_received": bytes_received,
                "packets_sent": packets_sent,
                "packets_received": packets_received,
                "upload_speed": upload_speed,
                "download_speed": download_speed,
            }
        )

    return {
        "hostname": hostname,
        "ip_address": ip_address,
        "interfaces": interfaces,
    }