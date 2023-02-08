# TD Ameritrade API

## TD Ameritrade API Alternative for Yahoo Finance
This code provides an alternative API for TD Ameritrade to the popular Yahoo Finance API. It retrieves historical daily price data for a specified stock symbol using the TDAmeritrade API and stores the data in a pandas dataframe.

Requirements

1- API Key for TD Ameritrade API
2- Selenium
3- Pandas
4- tda-api

To install the required packages, you can use the following command after navigating to the code directory in your terminal:

'''
pip install -r requirements.txt
'''

Environment Variables
Before running the code, you need to set the following environment variables:
create .env file then : 
API_KEY: Your TD Ameritrade API key
REDIRECT_URI: The URI to redirect to after authentication
TOKEN_PATH: The file path to store the access token
CHROME_USER_PROFILE: The file path to the Chrome user profile

Running the Code
You can run the code by using the following command in your terminal after navigating to the code directory:
'''
python main.py
'''
The code will retrieve the historical daily price data for the stock symbol AAPL and print the data stored in the pandas 
