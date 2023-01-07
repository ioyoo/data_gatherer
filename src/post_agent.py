import requests
import json


class PostAgent:
    URL = ""

    def __init__(self, post_url) -> None:
        self.URL = post_url

    def post(self, data):
        try:
            request = requests.post(self.URL, json=json.dumps(data))
            print(request.status_code)
        except ConnectionRefusedError as e:
            print("data could not be posted, connection refused! \n")
