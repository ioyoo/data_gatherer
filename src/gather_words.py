from data.credentials import APICredentials, RedditData
import requests
import time
import json
import os

stocks = RedditData()
creds = APICredentials()

tickers = stocks.get_top100()

dict = {}
print("Starting Info Download...")
time.sleep(3)
for i, ticker in enumerate(tickers):
    os.system('cls')
    print(f'[{i*"*"}{(len(tickers)-i)*" "}]')
    if i != 0 and i % 5 == 0:
        time.sleep(70)
    url = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={ticker}&apikey={creds.APLHA_VANTAGE}'
    dict[ticker] = requests.get(url).json()['Description']

path = os.path.join(os.getcwd(), "ticker_info.json")
with open(path, "w") as f:
    f.write(json.dumps(dict))

print(f"Finished recollecting data, new file: {path}" )
