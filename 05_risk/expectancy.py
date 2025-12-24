win_rate = 0.4
avg_win = 300
avg_loss = 100  # positive number

loss_rate = 1 - win_rate

expectancy = (win_rate * avg_win) - (loss_rate * avg_loss)

print("Expectancy per trade:", expectancy)
