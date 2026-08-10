import requests

API_URL = "http://127.0.0.1:8000/api/v1/metrics/"


def send_metrics(data):
    response = requests.post(API_URL, json=data)

    print(f"Status: {response.status_code}")

    try:
        print(f"Response: {response.json()}")
    except Exception:
        print(f"Response: {response.text}")