import requests

API_URL = "http://127.0.0.1:8000/api/v1/heartbeat/"


def send_heartbeat(hostname):

    requests.post(
        API_URL,
        json={
            "hostname": hostname,
        },
    )