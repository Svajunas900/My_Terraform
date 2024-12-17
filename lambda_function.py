from botocore.vendored import requests


def lambda_handler(event, context):
    response = requests.get("https://127.0.0.1:8000/prices/msft")
    print(response.json())
    return response.json()