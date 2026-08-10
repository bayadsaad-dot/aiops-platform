import requests

API_URL = "http://127.0.0.1:8000/api/v1/network/metrics/"


def send_network(data):

    hostname = data["hostname"]

    for interface in data["interfaces"]:

        payload = {
            "hostname": hostname,
            "interface_name": interface["name"],

            "bytes_sent": interface["bytes_sent"],
            "bytes_received": interface["bytes_received"],

            "packets_sent": interface["packets_sent"],
            "packets_received": interface["packets_received"],

            "upload_speed": interface["upload_speed"],
            "download_speed": interface["download_speed"],
        }

        response = requests.post(
            API_URL,
            json=payload,
        )

        print(
            f"{interface['name']} -> {response.status_code}"
        )

        if response.status_code != 201:
            print(response.text)