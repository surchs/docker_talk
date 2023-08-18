import time
import requests

print("hello world")


def hello(port: int) -> None:
    try:
        response = requests.get(f"http://container_a:{port}")
        if response.status_code == 200:
            print(f"Request to container_a on port {port} succeeded!")
        else:
            print(f"Request to container_a on port {port} failed with status code:", response.status_code)
    except requests.ConnectionError:
        print(f"Failed to connect to container_a on port {port}")




while True:
    hello(9000)
    hello(8000)
    
    time.sleep(5)
