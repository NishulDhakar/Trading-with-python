prices = [100, 102, 101, 103, 105, 104, 106, 108]

in_trade = False
entry_price = None

for price in prices:

    # ENTRY LOGIC
    if not in_trade and price > 104:
        entry_price = price
        in_trade = True
        print(f"ENTER trade at {entry_price}")

    # EXIT LOGIC
    elif in_trade and price < entry_price - 2:
        print(f"EXIT trade at {price}")
        in_trade = False
        entry_price = None

    else:
        print("No action")
