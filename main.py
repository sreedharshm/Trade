import time
import pandas as pd
from stock_data import download_stock_data  # Import the stock downloading function
from all_stock_list import get_nse_stock_symbols  # Import the function to get stock symbols

def batch_download(tickers,total, period='9mo', interval='1d', batch_size=5, delay=5):
    """
    Fetches stock data for a list of tickers in batches.

    Args:
        tickers (list): List of stock tickers to download.
        period (str): The period of data to fetch (e.g., '1mo', '6mo', '1y').
        interval (str): The data interval (e.g., '1d', '1h', '5m').
        batch_size (int): Number of tickers to process in each batch.
        delay (int): Time delay between batches in seconds.

    Returns:
        pd.DataFrame: DataFrame containing the stock data for all tickers.
    """
    # all_data = pd.DataFrame()  # Initialize an empty DataFrame to store all data
    completed=0
    # Process tickers in batches
    for i in range(0, len(tickers), batch_size):
        batch = tickers[i:i + batch_size]  # Create a batch of tickers
        print(f"Processing batch: {batch}")
        
        # Fetch data for each ticker in the current batch
        for ticker in batch:
            try:
                data,code = download_stock_data(ticker, period=period, interval=interval)
                if(code==1):
                    delay=delay-1.66666
                # all_data = pd.concat([all_data, data])  # Append the data to the master DataFrame
            except Exception as e:
                print(f"Failed to download data for {ticker}: {e}")
        completed+=3
        # Introduce a delay between batches
        print(f"Batch completed : {completed}/{total}. Sleeping for {delay} seconds...")
        time.sleep(delay)
        delay=5

    return "Completed"

# Example usage
nse_tickers = get_nse_stock_symbols('EQUITY_L.csv')  # Provide the path to your CSV file
total=len(nse_tickers)
# Call the batch download function
stock_data = batch_download(nse_tickers,total, period='max', interval='1d', batch_size=3, delay=5,)

# Output the result (this will print the DataFrame or a summary of the data)
print(stock_data)
