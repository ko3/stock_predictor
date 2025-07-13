# data/collect.py

import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import os

def download_stock_data(symbol="AAPL", days_back=365):
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days_back)

    df = yf.download(symbol, start=start_date.strftime('%Y-%m-%d'), end=end_date.strftime('%Y-%m-%d'))
    df.reset_index(inplace=True)

    os.makedirs("data/raw", exist_ok=True)
    df.to_csv(f"data/raw/{symbol}.csv", index=False)
    print(f"Downloaded {symbol} data to data/raw/{symbol}.csv")

if __name__ == "__main__":
    download_stock_data()
