entry_price = 100
stop_loss = 98
take_profit = 106

risk = entry_price - stop_loss
reward = take_profit - entry_price

rr_ratio = reward / risk

print("Risk:", risk)
print("Reward:", reward)
print("Risk-Reward Ratio:", rr_ratio)
