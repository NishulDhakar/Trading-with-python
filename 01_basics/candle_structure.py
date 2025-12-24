# One OHLC candle as a dictionary

candle = {
    "open": 100,
    "high": 110,
    "low": 95,
    "close": 105
}

if candle["close"] > candle["high"] -2:
    print("strong bullish")
elif candle["close"] < candle["low"] + 2:
    print("strong bearish")
else:
    print("normal")