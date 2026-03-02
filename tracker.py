import yfinance as yf
import pandas as pd
from datetime import datetime
import os

# -----------------------------
# Fetch data
# -----------------------------
dr = yf.Ticker("DRREDDY.NS")
airtel = yf.Ticker("BHARTIARTL.NS")
nifty = yf.Ticker("^NSEI")

today = datetime.now().strftime("%Y-%m-%d")

# Get closing prices
dr_price = dr.history(period="1d")['Close'].iloc[-1]
airtel_price = airtel.history(period="1d")['Close'].iloc[-1]
nifty_price = nifty.history(period="1d")['Close'].iloc[-1]

# -----------------------------
# FILE 1: Dr Reddy + Nifty
# -----------------------------
file1 = "market_data1.csv"

data1 = pd.DataFrame([[today, dr_price, nifty_price]],
                     columns=["Date", "Dr_Reddy", "Nifty50"])

if os.path.exists(file1):
    data1.to_csv(file1, mode="a", header=False, index=False)
else:
    data1.to_csv(file1, index=False)

# -----------------------------
# FILE 2: Airtel + Nifty
# -----------------------------
file2 = "market_data2.csv"

data2 = pd.DataFrame([[today, airtel_price, nifty_price]],
                     columns=["Date", "Airtel", "Nifty50"])

if os.path.exists(file2):
    data2.to_csv(file2, mode="a", header=False, index=False)
else:
    data2.to_csv(file2, index=False)

# -----------------------------
# Print logs (for GitHub Actions)
# -----------------------------
print(f"Saved {today}")
print(f"Dr Reddy: {dr_price}")
print(f"Airtel: {airtel_price}")
print(f"Nifty50: {nifty_price}")