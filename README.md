# TD Ameritrade API
---
#### TD Ameritrade API Alternative for Yahoo Finance
---
This code is able to fetch historical data via API from your TdAmeritrade ,it is more accurte than Yahoo Finance API. It retrieves historical per minte , hour , day ,week or month  for a specified stock symbol using the TDAmeritrade API and stores the data in a pandas dataframe.

***Requirements :***

1- API Key for TD Ameritrade API
2- Selenium
3- Pandas
4- tda-api

To install the required packages, you can use the following command after navigating to the code directory in your terminal:

```
pip install -r requirements.txt
```
Environment Variables
Before running the code, you need to set the following environment variables inside the .env file 
```
touch .env
```
and put inside it : 
```
#Your TD Ameritrade API key
API_KEY= "your-api-code"
#this should be 
REDIRECT_URI = "https://localhost/"
# Google chrome profile path
CHROME_USER_PROFILE="path/to/profile"
# leave it as is
TOKEN_PATH = "td-credentials.json"
```

Running the Code
You can run the code by using the following command in your terminal after navigating to the code directory:
```
python main.py
```
The code will retrieve the historical daily price data for the stock symbol AAPL and print the data stored in the pandas 
