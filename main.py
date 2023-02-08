import atexit
import tda
import json
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

API_KEY = os.getenv("API_KEY")
REDIRECT_URI = os.getenv("REDIRECT_URI")
TOKEN_PATH = os.getenv("TOKEN_PATH")
chrome_user_profile = os.getenv("CHROME_USER_PROFILE")


def make_webdriver():
    # Import selenium here because it's slow to import
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options

    # set chrome options
    options = webdriver.ChromeOptions()
    options.add_argument(r"--user-data-dir=" + chrome_user_profile)
    driver = webdriver.Chrome(options=options)
    atexit.register(lambda: driver.quit())
    return driver


ticker = "AAPL"
# Create a new client
clienttda = tda.auth.easy_client(API_KEY, REDIRECT_URI, TOKEN_PATH, make_webdriver)
# get price history every day
r = clienttda.get_price_history_every_day(ticker)
# Check if the request was successful
assert r.status_code == 200, r.raise_for_status()
# store OHLCV data in a dataframe
data = json.dumps(r.json()["candles"], indent=4)
# load json data into a dataframe
df = pd.read_json(data)
# print the dataframe
print(df)
