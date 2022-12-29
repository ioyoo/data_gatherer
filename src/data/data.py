import yaml
import os


class RedditData:
    CHANNELS = ["stockmarket", "wallstreetbets", "investing",
                "dividends", "investing_discussion", "stocks"]
    KEYWORDS = ["TSLA", "APPL", "GOO", "HP", "tesla", "elon"]

    def __init__(self, channels=CHANNELS, keywords=KEYWORDS):
        self.CHANNELS = channels
        self.KEYWORDS = keywords

    def set_channels(self, channels):
        self.CHANNELS = channels

    def set_keywords(self, keywords):
        self.KEYWORDS = keywords


class RedditCredentials:
    SECRET = ""
    CLIENT_AUTH2 = ""
    USER_AGENT = ""
    CRED_PATH = 'src\private\credentials.yaml'

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
