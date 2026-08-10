import requests


def send_processes(
    backend_url: str,
    hostname: str,
    processes: list,
):
    response = requests.post(
        f"{backend_url}/api/v1/processes/{hostname}",
        json=processes,
        timeout=10,
    )

    print("Status:", response.status_code)
    print("Response:", response.text)

    response.raise_for_status()

    return response.json()