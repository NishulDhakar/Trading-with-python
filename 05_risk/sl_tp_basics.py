entry_price = 100
stop_loss = 95
take_profit = 110

current_price = 108

if current_price <= stop_loss:
    print("Stop-loss hit → Exit trade")
elif current_price >= take_profit:
    print("Take-profit hit → Exit trade")
else:
    print("Hold trade")
