import os, pandas
import plotly.graph_objects as go
from plotly.offline import iplot


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

    # BB lower line
    df['lowerband'] = df['20sma'] + (2 * df['stddev'])
    # BB upper line
    df['upperband'] = df['20sma'] - (2 * df['stddev'])

    if symbol in symbols:
        print(df)
        aapl_df = df

candlestick = go.Candlestick(x=df['Date'], open=aapl_df['Open'], high=aapl_df['High'], low=aapl_df['Low'], close=aapl_df['Close'])

fig = go.Figure([
    
            ])
# iplot(fig)
fig.show()