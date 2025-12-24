# Trade log (list of completed trades)
trade_log = []

# Simulate a trade
entry_price = 100
exit_price = 108
quantity = 50

pnl = (exit_price - entry_price) * quantity

trade = {
    "entry": entry_price,
    "exit": exit_price,
    "quantity": quantity,
    "pnl": pnl
}

trade_log.append(trade)

total_pnl = 0
wins = 0
losses = 0

for trade in trade_log:
    total_pnl += trade["pnl"]

    if trade["pnl"] > 0:
        wins += 1
    else:
        losses += 1

print("Total PnL:", total_pnl)
print("Wins:", wins)
print("Losses:", losses)
