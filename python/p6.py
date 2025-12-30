# 1. Take Inputs
cap = float(input("Enter capacity in liters: "))
rate = float(input("Enter the leakage rate in ml/sec: "))
days = int(input("Enter the number of days: "))

# 2. Convert Capacity from Liters to Milliliters
total_water_ml = cap * 1000

# 3. Convert Days to Seconds
# (Days * 24 hours * 60 minutes * 60 seconds)
total_seconds = days * 24 * 60 * 60

# 4. Calculate Total Loss in Milliliters
total_loss_ml = rate * total_seconds

# 5. Calculate Remaining Water in Milliliters
# Logic: Starting Amount - Amount Lost
remaining_ml = total_water_ml - total_loss_ml

# 6. Convert Remaining Water back to Liters
remaining_liters = remaining_ml / 1000

# 7. Output the result
# We add a check: if result is negative, it means the tank is empty.
if remaining_liters < 0:
    print("The tank is empty (0 Liters remaining).")
else:
    print(f"Remaining water: {remaining_liters} Liters")
