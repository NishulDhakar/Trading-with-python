# Candle history (multiple candles)

candles = [
    {"open": 100, "high": 105, "low": 98, "close": 104},
    {"open": 104, "high": 108, "low": 102, "close": 107},
    {"open": 107, "high": 110, "low": 105, "close": 106},
    {"open": 106, "high": 109, "low": 103, "close": 108},
]


for candle in candles:
    if candle["close"] > candle["high"] - 2:
        print("strong bullish", candle)
    else:
        print("normal")

