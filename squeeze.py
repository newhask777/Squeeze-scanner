import os, pandas
import plotly


symbols = ['AAPL']

for filename in os.listdir('datasets'):
    # print(filename)
    symbol = filename.split(".")[0]
    # print(symbol)
    df = pandas.read_csv('datasets/{}'.format(filename))
    # print(df)
    if df.empty:
        continue


    # Simple Moving avg
    df['20sma'] = df['Close'].rolling(window=20).mean()

    # Standart deviation
    df['stddev'] = df['Close'].rolling(window=20).std()

    if symbol in symbols:
        print(df)