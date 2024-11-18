"""
This script calculates the volatility, annualized volatility, and beta of a portfolio based on the daily returns of
individual stocks. The script assumes that the daily return data for each stock is stored in separate CSV files in a
specified data folder. The script also requires the daily return data for the S&P 500 index to calculate the portfolio's
beta. The portfolio composition is defined by the weight of each stock in the portfolio.
:author: Or Forshmit
"""

import pandas as pd
import os

# Set the path to your data folder
data_folder = 'example_data'

# Define the example_weights based on your portfolio composition
# Format is: 'Stock Symbol': Weight
example_weights = {
    'VOO': 0.4958, 'JPM': 0.1047, 'RSP': 0.0832, 'NVDA': 0.0652,
    'MSFT': 0.0594, 'LLY': 0.0416, 'JEPQ': 0.0386, 'ANET': 0.0364,
    'BRK-B': 0.0213, 'PLTR': 0.0209, 'ORCL': 0.008, 'ENSG': 0.0071,
    'TMHC': 0.0065, 'CMG': 0.0056, 'HIMS': 0.0032, 'ASTS': 0.0025
}

# Make sure that the weights sum to 1 (0.99... is fine due to floating-point precision)
weights_sum = sum(example_weights.values())
if abs(weights_sum - 1) > 1e-10:
    raise ValueError("Weights do not sum to 1. Sum of Weights:", weights_sum)

def load_and_process(f_path):
    """
    Load stock data from a CSV file and process it to calculate daily returns.
    :param f_path: The file path to the CSV file.
    :return: A DataFrame with Date as the index and Daily Return as a column.
    """
    df = pd.read_csv(f_path)
    df['Date'] = pd.to_datetime(df['Date'], format='%b %d, %Y')  # Adjust for "Oct 25, 2024" format
    df = df.sort_values('Date')

    # Convert 'Adj Close**' column to numeric, ignoring commas, and handling missing values
    df['Adj Close'] = pd.to_numeric(df['Adj Close**'].replace({',': ''}, regex=True), errors='coerce')

    # Filter out rows with NaN in 'Adj Close', which we assume to be dividend rows
    df = df.dropna(subset=['Adj Close'])

    # Calculate daily returns using only the adjusted close prices
    df['Daily Return'] = df['Adj Close'].pct_change()

    # Return only Date and Daily Return columns with Date as the index
    return df[['Date', 'Daily Return']].set_index('Date')


# Load all stock data into a dictionary
stock_data = {}
for file_name in os.listdir(data_folder):
    if file_name.endswith('.csv') and file_name != 'benchmark.csv':
        stock_name = file_name.split('.')[0]
        file_path = os.path.join(data_folder, file_name)
        stock_data[stock_name] = load_and_process(file_path)

# Load benchmark data for benchmark
benchmark_data = load_and_process(os.path.join(data_folder, 'benchmark.csv'))

# Merge daily returns of all stocks by date
all_data = pd.concat([stock_data[stock].rename(columns={'Daily Return': stock}) for stock in stock_data], axis=1)
all_data.dropna(inplace=True)  # Drop any rows with missing data

# Calculate weighted portfolio returns
all_data['Portfolio Return'] = sum(example_weights[stock] * all_data[stock] for stock in example_weights)

# Calculate benchmark volatility
benchmark_volatility = benchmark_data['Daily Return'].std()
print("Benchmark Volatility:", benchmark_volatility)

# Calculate portfolio volatility
portfolio_volatility = all_data['Portfolio Return'].std()
print("Portfolio Volatility:", portfolio_volatility)

# Calculate annualized volatilities
annualized_benchmark_volatility = benchmark_volatility * (252 ** 0.5)
annualized_portfolio_volatility = portfolio_volatility * (252 ** 0.5)
print("Annualized Benchmark Volatility:", annualized_benchmark_volatility)
print("Annualized Portfolio Volatility:", annualized_portfolio_volatility)

# Calculate portfolio beta
all_data = all_data.join(benchmark_data.rename(columns={'Daily Return': 'benchmark Return'}), how='inner')
beta = all_data['Portfolio Return'].cov(all_data['benchmark Return']) / all_data['benchmark Return'].var()
print("Portfolio Beta:", beta)
