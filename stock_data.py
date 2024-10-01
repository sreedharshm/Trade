# data_acquire.py
import yfinance as yf
import pandas as pd

import os
import pandas as pd
import yfinance as yf
from datetime import datetime

def download_stock_data(ticker, period='1mo', interval='1d'):
    """
    Downloads stock data for a single ticker and caches it in a CSV file.
    If the CSV file exists and was fetched today, no new request is made.

    Args:
        ticker (str): Stock ticker symbol (e.g., 'RELIANCE.NS').
        period (str): The period for which data is needed (e.g., '1mo', '6mo', '1y').
        interval (str): The interval for the stock data (e.g., '1d', '5m').

    Returns:
        pd.DataFrame: DataFrame containing the stock data.
    """
    # File path to save the CSV
    tickername=ticker.replace('.NS', '')
    csv_file = os.path.join('data', f"{tickername}.csv")
    
    # Check if CSV file already exists
    if os.path.exists(csv_file):
        # Load the existing data
        existing_data = pd.read_csv(csv_file)
        
        # Check if the CSV file has data from today
        last_date = pd.to_datetime(existing_data['Date']).max().date()
        if last_date == datetime.today().date():
            print(f"Data for {ticker} is already up-to-date.")
            return existing_data,1
    
    # If no file or outdated data, fetch new data from yfinance
    print(f"Fetching new data for {ticker} from API...")
    new_data = yf.download(ticker, period=period, interval=interval)

    if not new_data.empty:
        # Save new data to CSV
        new_data.to_csv(csv_file)
        print(f"Data for {ticker} saved to {csv_file}.")
    
    return new_data,0
