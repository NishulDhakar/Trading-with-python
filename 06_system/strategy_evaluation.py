# Example trade log
trade_log = [
    {"pnl": 500},
    {"pnl": -200},
    {"pnl": 600},
    {"pnl": -300},
    {"pnl": 400},
]

total_trades = len(trade_log)
wins = 0
losses = 0
total_win = 0
total_loss = 0

for trade in trade_log:
    if trade["pnl"] > 0:
        wins += 1
        total_win += trade["pnl"]
    else:
        losses += 1
        total_loss += abs(trade["pnl"])

win_rate = wins / total_trades
avg_win = total_win / wins if wins > 0 else 0
avg_loss = total_loss / losses if losses > 0 else 0

expectancy = (win_rate * avg_win) - ((1 - win_rate) * avg_loss)

print("Total Trades:", total_trades)
print("Win Rate:", win_rate)
print("Average Win:", avg_win)
print("Average Loss:", avg_loss)
print("Expectancy:", expectancy)
