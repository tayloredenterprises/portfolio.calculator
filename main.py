import crypto_values 
import commodity_values
import stock_values
import gsheet_api
import time

print("\033[1;33m\n")
print("Crypto")
print(gsheet_api.crypto1_symbol + ' = $' + str(crypto_values.crypto1_market_value))
time.sleep(0.4)

print("\033[1;36m")
print("Commodities")
print("Gold" + ' = $' + str(commodity_values.gold_result))
time.sleep(0.4)

print("\033[1;35m")
print("Stocks")
print(gsheet_api.stock1_symbol + ' = $' + str(stock_values.stock1_market_value))
time.sleep(0.4)
print(gsheet_api.stock2_symbol + ' = $' + str(stock_values.stock2_market_value))
time.sleep(0.4)
print(gsheet_api.stock3_symbol + ' = $' + str(stock_values.stock3_market_value))
time.sleep(0.4)
print(gsheet_api.stock4_symbol + ' = $' + str(stock_values.stock4_market_value))
time.sleep(0.4)
print(gsheet_api.stock5_symbol + ' = $' + str(stock_values.stock5_market_value))

totals = crypto_values.crypto1_market_value + commodity_values.gold_result + stock_values.stock1_market_value + stock_values.stock2_market_value + stock_values.stock3_market_value + stock_values.stock4_market_value + stock_values.stock5_market_value
print("\033[1;32m")
print("Total = $" + str(totals))
print("")