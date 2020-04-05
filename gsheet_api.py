from __future__ import print_function
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# If modifying these scopes, delete the file credentials.json.
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'

# The ID and range of spreadsheet.
SPREADSHEET_ID = '<SPREADSHEET_ID>'

# The file credentials.json stores the user's access and
# refresh tokens, and is created automatically when the 
# authorization flow completes for the first time.
store = file.Storage('credentials.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('sheets', 'v4', http=creds.authorize(Http()))

# fetch information in cells B10 and C10
def gsheet_crypto1():
    RANGE_NAME = 'Stocks!B10:C10'

    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                range=RANGE_NAME).execute()
    values = result.get('values', [])
    if not values:
        print('No data found.')
    for row in values:
        return ('%s, %s' % (row[0], row[1]))

if __name__ == '__gsheet_crypto1__':
     gsheet_crypto1()

# fetch information in cells B2 and C2
def gsheet_stock1():
    RANGE_NAME = 'Stocks!B2:C2'

    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                range=RANGE_NAME).execute()
    values = result.get('values', [])
    if not values:
        print('No data found.')
    else:
        for row in values:
            return ('%s, %s' % (row[0], row[1]))

if __name__ == '__gsheet_stock1__':
     gsheet_stock1()

# fetch information in cells B3 and C3
def gsheet_stock2():
    RANGE_NAME = 'Stocks!B3:C3'

    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                range=RANGE_NAME).execute()
    values = result.get('values', [])
    if not values:
        print('No data found.')
    else:
        for row in values:
            return ('%s, %s' % (row[0], row[1]))

if __name__ == '__gsheet_stock2__':
     gsheet_stock2()

# fetch information in cells B4 and C4
def gsheet_stock3():
    RANGE_NAME = 'Stocks!B4:C4'

    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                range=RANGE_NAME).execute()
    values = result.get('values', [])
    if not values:
        print('No data found.')
    else:
        for row in values:
            return ('%s, %s' % (row[0], row[1]))

if __name__ == '__gsheet_stock3__':
     gsheet_stock3()

# fetch information in cells B5 and C5
def gsheet_stock4():
    RANGE_NAME = 'Stocks!B5:C5'

    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                range=RANGE_NAME).execute()
    values = result.get('values', [])
    if not values:
        print('No data found.')
    else:
        for row in values:
            return ('%s, %s' % (row[0], row[1]))

if __name__ == '__gsheet_stock4__':
     gsheet_stock4()

# fetch information in cells B6 and C6
def gsheet_stock5():
    RANGE_NAME = 'Stocks!B6:CB6'

    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                range=RANGE_NAME).execute()
    values = result.get('values', [])
    if not values:
        print('No data found.')
    else:
        for row in values:
            return ('%s, %s' % (row[0], row[1]))

if __name__ == '__gsheet_stock5__':
     gsheet_stock5()

# fetch information in cells B8 and C8
def gsheet_gold():
    RANGE_NAME = 'Stocks!B8:C8'

    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                range=RANGE_NAME).execute()
    values = result.get('values', [])
    if not values:
        print('No data found.')
    else:
        for row in values:
            return ('%s, %s' % (row[0], row[1]))

if __name__ == '__gsheet_gold__':
     gsheet_gold()

# split returned data into a string and a float
crypto1_results = gsheet_crypto1()
crypto1_symbol,crypto1_value = crypto1_results.split(', ', 1)
converted_crypto1_holdings = float(crypto1_value)

stock1_results = gsheet_stock1()
stock1_symbol,stock1_value = stock1_results.split(', ', 1)
converted_stock1_holdings = float(stock1_value)

stock2_results = gsheet_stock2()
stock2_symbol,stock2_value = stock2_results.split(', ', 1)
converted_stock2_holdings = float(stock2_value)

stock3_results = gsheet_stock3()
stock3_symbol,stock3_value = stock3_results.split(', ', 1)
converted_stock3_holdings = float(stock3_value)

stock4_results = gsheet_stock4()
stock4_symbol,stock4_value = stock4_results.split(', ', 1)
converted_stock4_holdings = float(stock4_value)

stock5_results = gsheet_stock5()
stock5_symbol,stock5_value = stock5_results.split(', ', 1)
converted_stock5_holdings = float(stock5_value)

gold_results = gsheet_gold()
gold_symbol,gold_value = gold_results.split(', ', 1)
converted_gold_holdings = float(gold_value)