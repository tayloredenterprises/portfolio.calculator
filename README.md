# Portfolio Calculator

To use this application, do the following:

1. Modify the tag '<>' in gsheet_api.py to use the desired Google spreadsheet ID.
2. Modify the endpoint URL's in stock_values.py to include your own Alpha Vantage API key.
3. Save your Google API client credentials file 'client_secret.json' in the script root directory. 
4. Create Google Sheet and ensure the name of the sheet matches the name defined in gsheet_api.py. Here the name is called "Stocks". 
5. Enter the required data in the Google Sheet, with the following format:
   * Column A - Friendly name for stock/commodity/crypto.
   * Column B - Five character stock code with dot point separator - i.e. 'NAB.AX'.
   * Column C - Integer/float value of number of shares/grams of gold/coins owned.
    
