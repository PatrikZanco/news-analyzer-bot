import requests


def valid_request(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return "success"
        else:
            return f"error: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"error: {e}"


