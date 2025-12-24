# Capital over time (equity curve)
capital_history = [
    100000,
    102000,
    101000,
    105000,
    98000,
    96000,
    99000,
    103000
]

peak = capital_history[0]
max_drawdown = 0

for capital in capital_history:
    if capital > peak:
        peak = capital

    drawdown = (peak - capital) / peak

    if drawdown > max_drawdown:
        max_drawdown = drawdown

print("Maximum Drawdown:", max_drawdown * 100, "%")
