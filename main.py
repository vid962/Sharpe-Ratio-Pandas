import numpy as np
import pandas_datareader as pdr
import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt

tickers = ['AAPL', 'MSFT', 'TWTR', 'IBM']
start = dt.datetime(2020, 1, 1)
data = pdr.get_data_yahoo(tickers, start)
data = data['Adj Close']

portfolio = [.25, .15, .40, .20]

# we can see the percentage change easily
print(data / data.shift())

# calculating the daily log return of the portfolio
log_return = np.sum(np.log(data / data.shift()) * portfolio, axis=1)

# visualisation of the daily log returns
fig, ax = plt.subplots()
log_return.hist(bins=50, ax=ax)

'''The Sharpe Ratio is the average return earned in excess of the risk-free rate 
    per unit of volatility or total risk.'''
sharpe_ratio = log_return.mean()/log_return.std()

# *we have 252 trading days, this give us annualized shape ratio
asr = sharpe_ratio*252**.5
plt.show()