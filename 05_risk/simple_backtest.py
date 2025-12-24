# Price history
closing_prices = [100, 102, 101, 103, 105, 104, 106, 103, 101, 99, 98, 100]

fast_period = 3
slow_period = 5

def calculate_sma(prices, period):
    if len(prices) < period:
        return None
    return sum(prices[-period:]) / period


# Loop over candles (this is a backtest)
for i in range(len(closing_prices)):
    prices_so_far = closing_prices[:i+1]


    prev_prices = prices_so_far[:-1]


    prev_fast = calculate_sma(prev_prices, fast_period)
    prev_slow = calculate_sma(prev_prices, slow_period)

    curr_fast = calculate_sma(prices_so_far, fast_period)
    curr_slow = calculate_sma(prices_so_far, slow_period)

    if prev_fast and prev_slow and curr_fast and curr_slow:
        if prev_fast <= prev_slow and curr_fast > curr_slow:
            print(f"Candle {i}: BUY signal at price {closing_prices[i]}")
        elif prev_fast >= prev_slow and curr_fast < curr_slow:
            print(f"Candle {i}: SELL signal at price {closing_prices[i]}")
