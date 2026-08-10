import requests

API_URL = "http://127.0.0.1:8000/api/v1/network/interfaces/sync"


def send_network(data):
    response = requests.post(API_URL, json=data)

    print(f"Network Status: {response.status_code}")

    try:
        print(response.json())
    except Exception:
        print(response.text)