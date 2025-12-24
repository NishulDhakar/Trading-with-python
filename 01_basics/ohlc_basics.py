# open_price = 100
# close_price = 105

# if close_price > open_price:
#     print("Green candle (Bullish)")
# else:
#     print("Red candle (Bearish)")

# Closing prices of last 5 candles
closing_prices = [100, 102, 101, 105, 108]

print("Closing prices:", closing_prices)


if closing_prices[0] < closing_prices[-1]:
    print("Bullish")
else:
    print("Bearish")