# Candle close prices (price history)
closing_prices = [100, 101, 101, 101, 101, 101, 100]

# SMA periods
fast_period = 2
slow_period = 6

# Helper function to calculate SMA
def calculate_sma(prices, period):
    if len(prices) < period:
        return None
    return sum(prices[-period:]) / period


# Calculate previous SMAs (one candle ago)
prev_prices = closing_prices[:-1]

prev_fast_sma = calculate_sma(prev_prices, fast_period)
prev_slow_sma = calculate_sma(prev_prices, slow_period)

# Calculate current SMAs
curr_fast_sma = calculate_sma(closing_prices, fast_period)
curr_slow_sma = calculate_sma(closing_prices, slow_period)

print("Previous Fast SMA:", prev_fast_sma)
print("Previous Slow SMA:", prev_slow_sma)
print("Current Fast SMA:", curr_fast_sma)
print("Current Slow SMA:", curr_slow_sma)

# Crossover logic
if prev_fast_sma is not None and prev_slow_sma is not None:
    if prev_fast_sma <= prev_slow_sma and curr_fast_sma > curr_slow_sma:
        print("BUY signal (Bullish crossover)")
    elif prev_fast_sma >= prev_slow_sma and curr_fast_sma < curr_slow_sma:
        print("SELL signal (Bearish crossover)")
    else:
        print("No crossover")
 