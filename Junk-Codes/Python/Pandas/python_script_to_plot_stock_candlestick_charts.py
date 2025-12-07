import yfinance as yf
import mplfinance as mpf
import pandas as pd

ticker = input("Enter stock name: ")
df = yf.download(ticker, start="2025-01-01", end="2025-12-01", auto_adjust=True)

if df.empty:
    print("No data found for the given stock ticker.")
else:
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)
    df = df[["Open", "High", "Low", "Close", "Volume"]]
    mpf.plot(
        df,
        type="candle",
        style="charles",
        title=f"{ticker.upper()} Candlestick Chart",
        ylabel="Price",
    )
