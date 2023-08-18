import time
import requests

print("hello world")

while True:
    try:
        response = requests.get("http://container_a:8000")
        if response.status_code == 200:
            print("Request to container_a succeeded!")
        else:
            print("Request to container_a failed with status code:", response.status_code)
    except requests.ConnectionError:
        print("Failed to connect to container_a")
    
    time.sleep(5)
