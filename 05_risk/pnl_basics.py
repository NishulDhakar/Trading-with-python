# Trade details
entry_price = 100
current_price = 105
quantity = 50

# Unrealized PnL
unrealized_pnl = (current_price - entry_price) * quantity

print("Unrealized PnL:", unrealized_pnl)

exit_price = 103

realized_pnl = (exit_price - entry_price) * quantity

print("Realized PnL:", realized_pnl)
