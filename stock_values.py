import requests
import json
import gsheet_api
import time
from string import Template

# returns the current AUD market price of stock1
# precision = the amount of decimal places to round to (default of 2)
def get_stock1_value(precision=2):
    # API for stock value
    s = Template('https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=${SYM}&interval=5min&apikey=<KEY>')
    d = dict(SYM=gsheet_api.stock1_symbol)
    api_endpoint = s.substitute(d)

    # fetch the content from the api
    try:
        response = requests.get(api_endpoint, timeout=5)
    except:
        return None

    #load the reponse from the api into a lookup object
    content_object = json.loads(response.content)

    # extract the price from the lookup
    price = content_object["Global Quote"]["05. price"]
    return float(price)

# round output from get_stock1_value
def stock1_rounded(precision=2):
    stocks = get_stock1_value() * gsheet_api.converted_stock1_holdings
    if stocks == None:
        return "uh-oh!"
    rounded_stocks = round(stocks, precision)
    return rounded_stocks
    
if __name__ == '__stock1_rounded__':
    stock1_rounded()

# returns the current AUD market price of stock2
# precision = the amount of decimal places to round to (default of 2)
def get_stock2_value(precision=2):
    s = Template('https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=${SYM2}&interval=5min&apikey=<KEY>')
    d = dict(SYM2=gsheet_api.stock2_symbol)
    api_endpoint = s.substitute(d)

    # fetch the content from the api
    try:
        response = requests.get(api_endpoint, timeout=20)
    except:
        return None

    #load the reponse from the api into a lookup object
    content_object = json.loads(response.content)

    # extract the price from the lookup
    price = content_object["Global Quote"]["05. price"]
    return float(price)

# round output from get_stock2_value
def stock2_rounded(precision=2):
    stocks = get_stock2_value() * gsheet_api.converted_stock2_holdings
    if stocks == None:
        return "uh-oh!"
    rounded_stocks = round(stocks, precision)
    return rounded_stocks
    
if __name__ == '__stock2_rounded__':
    stock2_rounded()

# returns the current AUD market price of stock3
# precision = the amount of decimal places to round to (default of 2)
def get_stock3_value(precision=2):
    # fetch the content from the api
    s = Template('https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=${SYM3}&interval=5min&apikey=<KEY>')
    d = dict(SYM3=gsheet_api.stock3_symbol)
    api_endpoint = s.substitute(d)

    try:
        response = requests.get(api_endpoint, timeout=5)
    except:
        return None

    #load the reponse from the api into a lookup object
    content_object = json.loads(response.content)

    # extract the price from the lookup
    price = content_object["Global Quote"]["05. price"]
    return float(price)

# round output from get_stock3_value
def stock3_rounded(precision=2):
    stocks = get_stock3_value() * gsheet_api.converted_stock3_holdings
    if stocks == None:
        return "uh-oh!"
    rounded_stocks = round(stocks, precision)
    return rounded_stocks
    
if __name__ == '__stock3_rounded__':
    stock3_rounded()
    
# returns the current AUD market price of stock4
# precision = the amount of decimal places to round to (default of 2)
def get_stock4_value(precision=2):
    s = Template('https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=${SYM4}&interval=5min&apikey=<KEY>')
    d = dict(SYM4=gsheet_api.stock4_symbol)
    api_endpoint = s.substitute(d)

    # fetch the content from the api
    try:
        response = requests.get(api_endpoint, timeout=5)
    except:
        return None

    #load the reponse from the api into a lookup object
    content_object = json.loads(response.content)

    # extract the price from the lookup
    price = content_object["Global Quote"]["05. price"]
    return float(price)

# round output from get_stock4_value
def stock4_rounded(precision=2):
    stocks = get_stock4_value() * gsheet_api.converted_stock4_holdings
    if stocks == None:
        return "uh-oh!"
    rounded_stocks = round(stocks, precision)
    return rounded_stocks

if __name__ == '__stock4_rounded__':
    stock4_rounded()


# returns the current AUD market price of stock5
# precision = the amount of decimal places to round to (default of 2)
def get_stock5_value(precision=2):
    s = Template('https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=${SYM5}&interval=5min&apikey=<KEY>')
    d = dict(SYM5=gsheet_api.stock5_symbol)
    api_endpoint = s.substitute(d)

    # fetch the content from the api
    try:
        response = requests.get(api_endpoint, timeout=5)
    except:
        return None

    #load the reponse from the api into a lookup object
    content_object = json.loads(response.content)

    # extract the price from the lookup
    price = content_object["Global Quote"]["05. price"]
    return float(price)

# round output from get_stock5_value
def stock5_rounded(precision=2):
    stocks = get_stock5_value() * gsheet_api.converted_stock5_holdings
    if stocks == None:
        return "uh-oh!"
    rounded_stocks = round(stocks, precision)
    return rounded_stocks

if __name__ == '__stock5_rounded__':
    stock5_rounded()

# store rounded values as variables
stock1_market_value = stock1_rounded()
stock2_market_value = stock2_rounded()
stock3_market_value = stock3_rounded()
stock4_market_value = stock4_rounded()
stock5_market_value = stock5_rounded()