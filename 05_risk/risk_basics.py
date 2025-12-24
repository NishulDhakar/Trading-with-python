# Account details
capital = 100_000
risk_percent = 1  # 1%

# Trade setup
entry_price = 100
stop_loss_price = 98

# Step 1: Calculate risk per trade
risk_amount = capital * (risk_percent / 100)

# Step 2: Risk per unit (per share)
risk_per_unit = entry_price - stop_loss_price

# Step 3: Position size
quantity = risk_amount / risk_per_unit

print("Risk amount:", risk_amount)
print("Risk per unit:", risk_per_unit)
print("Quantity to trade:", int(quantity))
