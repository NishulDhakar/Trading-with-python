prices = [100, 102, 101, 103, 105, 104, 106, 100, 102, 106, 108]

in_trade = False
entry_price = None

cooldown = 2        # wait 2 candles after exit
cooldown_counter = 0

for i, price in enumerate(prices):

    # Handle cooldown
    if cooldown_counter > 0:
        cooldown_counter -= 1
        print(f"Candle {i}: Cooldown ({cooldown_counter} left)")
        continue

    # ENTRY
    if not in_trade and price >= 105:
        in_trade = True
        entry_price = price
        print(f"Candle {i}: ENTER trade at {price}")

    # EXIT
    elif in_trade and price < entry_price - 2:
        in_trade = False
        cooldown_counter = cooldown
        print(f"Candle {i}: EXIT trade at {price} → cooldown starts")

    else:
        print(f"Candle {i}: No action")
