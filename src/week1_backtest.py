# -------------------------------
# Week 1 Mini-Task: Trading Simulation with ROI
# -------------------------------

# Step 1: Initial capital
capital = 1000  # starting money

# Step 2: Daily ROI percentages (as decimals, e.g., 0.05 = 5%)
daily_roi = [0.05, -0.02, 0.03, 0.01, -0.04, 0.06]

# Step 3: Function to calculate profit from capital and ROI
def calculate_profit(capital, roi):
    """
    Calculate profit based on capital and ROI
    Arguments:
        capital : float - current capital
        roi     : float - daily return on investment (decimal)
    Returns:
        float : profit amount
    """
    profit = capital * roi
    return profit

# Step 4: Function to process trade result
def trade_result(capital, profit):
    """
    Update capital based on profit/loss and return descriptive message
    Arguments:
        capital : float - current capital
        profit  : float - profit/loss for the day
    Returns:
        tuple: updated capital, message string
    """
    capital += profit
    status = "Profit" if profit > 0 else "Loss"
    message = f"{status}: {profit:.2f}, New Capital: {capital:.2f}"
    return capital, message

# Step 5: Run simulation and track stats
total_profit = 0
total_loss = 0
wins = 0
days = len(daily_roi)

print("Daily Trading Simulation with ROI:")

for day, roi in enumerate(daily_roi, start=1):
    profit = calculate_profit(capital, roi)
    capital, message = trade_result(capital, profit)
    print(f"Day {day}: {message}")

    if profit > 0:
        total_profit += profit
        wins += 1
    else:
        total_loss += profit

# Step 6: Summary statistics
win_rate = wins / days * 100
print("\n--- Simulation Summary ---")
print(f"Final Capital: {capital:.2f}")
print(f"Total Profit: {total_profit:.2f}")
print(f"Total Loss: {total_loss:.2f}")
print(f"Win Rate: {win_rate:.2f}%")
