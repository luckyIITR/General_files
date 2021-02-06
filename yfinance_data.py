import yfinance as yf
from datetime import datetime, timedelta


# get Intraday data for last 60 days
def Daily_data(symbol, interval="1d"):
    symbol = symbol + ".NS"
    data = yf.download(tickers=symbol, interval=interval, start=(datetime.now() - timedelta(days=50)),
                       end=datetime.now())
    data.index = data.index.tz_localize(None)
    return data
