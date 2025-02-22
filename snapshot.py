import os
import yfinance as yf


with open('symbols.csv') as f:
    lines = f.read().splitlines()
    # print(lines)
    for symbol in lines:
        print(symbol)
        data = yf.download(symbol, start="2024-01-01", end="2024-07-19")
        data.to_csv("datasets/{}.csv".format(symbol))


