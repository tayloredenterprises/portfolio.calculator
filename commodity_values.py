from bs4 import BeautifulSoup
import requests
import gsheet_api

# fetch gold data in $AUD
def get_gold_price():

    def get_dollar_figure(stringValue):
        # if we don't have a dollar sign return nothing
        if "$" not in stringValue:
            return None
        return "$" + stringValue.split('$', 1)[-1]

    page_link = 'https://www.abcbullion.com.au/products-pricing/gold#'

    # fetch the content from url
    page_response = requests.get(page_link, timeout=5)

    # parse html
    page_content = BeautifulSoup(page_response.content, "html.parser")

    # extract all html elements where price is stored
    # prices = page_content.find_all(class_='au')
    # you can also access the main_price class by specifying the tag of the class
    prices = page_content.find_all('div', attrs={'class':'au'})

    for price in prices:
        dollar_figure = get_dollar_figure(price.get_text())
        
        # once we get something back which is a dollar figure, we have our price
        if dollar_figure != None:
            return dollar_figure
            
# format output of get_gold_price()
# fetch gold holdings from the google sheet using gsheet_api.py
# multiply current gold price by number of grams held
def gold():
    #Tuple [1:6] prints just the figure         
    with_comma = get_gold_price()[1:6]
    nil_comma = with_comma.replace(',','')

    #define amt of grams gold held
    grams_gold = gsheet_api.converted_gold_holdings
    #convert price of ounce to price per gram
    conversion = int(nil_comma) / 28.35
    result = int(conversion) * grams_gold
    return result

# store result of gold() as a variable.
gold_result = gold()

if __name__ == '__gold__':
     gold() 
     

