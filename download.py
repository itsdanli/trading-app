import yfinance

df = yfinance.download('AAPL', start='2020-01-01', end='2020-02-01')
print(df)