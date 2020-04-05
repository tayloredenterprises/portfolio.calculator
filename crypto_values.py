import requests
import json
import gsheet_api
from string import Template

# returns the current AUD market price of crytocurrency coin
# args:
# precision: the amount of decimal places to round to (default of 2)
def get_crypto1_value(precision=2):
    s = Template('https://api.coingecko.com/api/v3/coins/${SYM}?localization=false&tickers=false&market_data=true&community_data=false&developer_data=false&sparkline=false')
    
    d = dict(SYM=gsheet_api.crypto1_symbol)
    api_endpoint = s.substitute(d)
    
    # fetch the content from the api
    try:
        response = requests.get(api_endpoint, timeout=5)
    except:
        return None
    # load the response from the api into a lookup object
    content_object = json.loads(response.content)

    # extract the price from the lookup
    price = content_object["market_data"]["current_price"]["aud"]
    return round(price, precision)

# return real dollar figure for the given amount of stocks fetched
# from stock_values.py
def crypto1_rounded(precision=2):
    value = get_crypto1_value() * gsheet_api.converted_crypto1_holdings
    if value == None:
        return "uh-oh!"
    rounded_value = round(value, precision)
    return rounded_value
    
# store result of rounded coin as variable
crypto1_market_value = crypto1_rounded()

if __name__ == '__crypto1_rounded__':
     crypto1_rounded()