# Candle history (close prices only)


candles = [
    {"close": 100},
    {"close": 102},
    {"close": 104},
    {"close": 103},
    {"close": 105},
]

window = 3

close_prices = [candle["close"] for candle in candles]

last_prices = close_prices[-window:]

print(type(last_prices[0]))

sma = sum(last_prices) / window
print("SMA:", sma)
