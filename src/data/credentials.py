import yaml
import os
import requests


class RedditData:
    CHANNELS = ["stockmarket", "wallstreetbets", "investing",
                "dividends", "investing_discussion", "stocks", "wallstreetbetsnew"]
    KEYWORDS = ["TSLA", "APPL", "GOO", "HP", "tesla", "elon"]

    def __init__(self, channels=CHANNELS, keywords=KEYWORDS):
        self.CHANNELS = channels
        self.KEYWORDS = keywords

    def get_top100(self):
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}
        res = requests.get(
            "https://api.nasdaq.com/api/quote/list-type/nasdaq100", headers=headers)
        self.KEYWORDS = [stock["symbol"]
                         for stock in res.json()['data']['data']['rows']]
        return self.KEYWORDS

    def set_channels(self, channels):
        self.CHANNELS = channels

    def set_keywords(self, keywords):
        self.KEYWORDS = keywords


class RedditCredentials:
    CRED_PATH = 'data_gatherer\src\private\credentials.yaml'
    SECRET = ""
    CLIENT_AUTH2 = ""
    USER_AGENT = ""

    def __init__(self, cred_path=CRED_PATH) -> None:
        self.CRED_PATH = cred_path
        cred_full_path = os.path.join(os.getcwd(), cred_path)
        with open(cred_full_path) as credentials_raw:
            try:
                credentials = yaml.safe_load(credentials_raw)
                self.SECRET = credentials['SECRET']
                self.CLIENT_AUTH2 = credentials['CLIENT_AUTH2']
                self.USER_AGENT = credentials['USER_AGENT']
            except yaml.YAMLError as exc:
                print(exc)

    def __repr__(self) -> str:
        return f' Secret: {self.SECRET}, Client Auth 2: {self.CLIENT_AUTH2}, User Agent: {self.USER_AGENT}, Path: {self.CRED_PATH}'


class APICredentials:
    CRED_PATH = 'data_gatherer\src\private\credentials.yaml'
    PATH = ''

    def __init__(self, cred_path=CRED_PATH) -> None:
        self.CRED_PATH = cred_path
        cred_full_path = os.path.join(os.getcwd(), cred_path)
        with open(cred_full_path) as credentials_raw:
            try:
                credentials = yaml.safe_load(credentials_raw)
                self.PATH = credentials['API_PATH']
            except yaml.YAMLError as exc:
                print(exc)

    def __repr__(self) -> str:
        return f' API_path: {self.PATH}'
