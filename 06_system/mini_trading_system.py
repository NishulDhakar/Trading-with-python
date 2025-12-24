# A trading system always follows this order:

# 1 Market data
# 2 Signal (Should I trade?)
# 3 Risk check (How much can I lose?)
# 4 Execution (Enter trade)
# 5 Management (SL / TP)
# 6 Result (PnL)

# -------------------------------
# 1. Market Data (closing prices)
# -------------------------------
prices = [110, 108, 106, 104, 102, 100, 103, 106, 111, 115]

# -------------------------------
# 2. Strategy Parameters
# -------------------------------

fast_period = 3
slow_period = 6

# -------------------------------
# 3. Risk Parameters
# -------------------------------
capital = 100_000
risk_percent = 1  # 1% risk per trade

# -------------------------------
# Helper: SMA calculation
# -------------------------------

def sma(prices, period):
    if len(prices) < period:
        return None
    return sum(prices[-period:]) / period


# -------------------------------
# 4. Trading Loop
# -------------------------------

in_trade = False

for i in range(len(prices)):
    price_history = prices[:i+1]
    prev_prices = price_history[:-1]

    prev_fast = sma(prev_prices, fast_period)
    prev_slow = sma(prev_prices, slow_period)

    curr_fast = sma(price_history, fast_period)
    curr_slow = sma(price_history, slow_period)

    current_price = prices[i]

    # ---------------------------
    # ENTRY LOGIC
    # ---------------------------

    if not in_trade and prev_fast and prev_slow and curr_fast and curr_slow:
        if prev_fast <= prev_slow and curr_fast > curr_slow:
            entry_price = current_price
            stop_loss = entry_price - 2
            take_profit = entry_price + 4

            risk_amount = capital * (risk_percent / 100)
            quantity = risk_amount / (entry_price - stop_loss)

            in_trade = True

            print(f"\nBUY at {entry_price}")
            print(f"SL: {stop_loss}, TP: {take_profit}")
            print(f"Quantity: {int(quantity)}")

    # ---------------------------
    # TRADE MANAGEMENT
    # ---------------------------

    if in_trade:
        if current_price <= stop_loss:
            pnl = (stop_loss - entry_price) * quantity
            capital += pnl
            in_trade = False
            print(f"STOP LOSS HIT at {current_price}, PnL: {pnl}")

        elif current_price >= take_profit:
            pnl = (take_profit - entry_price) * quantity
            capital += pnl
            in_trade = False
            print(f"TAKE PROFIT HIT at {current_price}, PnL: {pnl}")

print("\nFinal Capital:", capital)
