import pandas as pd

def get_nse_stock_symbols(file_path):
    """
    Reads a CSV file containing NSE stock symbols in the first column,
    appends '.NS' to each symbol, and returns a list of formatted stock symbols.

    Args:
        file_path (str): Path to the CSV file containing stock symbols.

    Returns:
        list: A list of stock symbols formatted for Yahoo Finance.
    """
    # Read the CSV file
    df = pd.read_csv(file_path)
    
    # Assuming the first column contains stock symbols
    stock_symbols = df.iloc[:, 0]  # Extract the first column (stock symbols)
    
    # Append '.NS' to each symbol
    nse_stock_symbols = [symbol.strip() + '.NS' for symbol in stock_symbols]
    
    return nse_stock_symbols

