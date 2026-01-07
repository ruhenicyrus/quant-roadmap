#Week 1 Mini-Task: Trading Simulation
# -------------------------------

# Step 1: Initial capital
capital = 1000  # starting money

# Step 2: Daily profits/losses
profits = [50, -20, 30, 10, -40, 60]

# Step 3: Function to calculate profit (could include ROI logic later)
def calculate_profit(capital, roi):
    """
    Calculate profit based on capital and ROI
    Arguments:
        capital : float/int - current capital
        roi     : float - return on investment (as decimal)
    Returns:
        profit : float - profit amount
    """
    profit = capital * roi
    return profit

# Step 4: Function to process trade result
def trade_result(capital, profit):
    """
    Update capital based on profit/loss and return a descriptive message
    """
    capital += profit  # update capital
    if profit > 0:
        message = f"Profit {profit}, new capital: {capital}"
    else:
        message = f"Loss {profit}, new capital: {capital}"
    return capital, message  # return updated capital AND message

# Step 5: Loop through daily profits/losses
print("Daily Trading Simulation:")
for p in profits:
    capital, message = trade_result(capital, p)  # update capital correctly
    print(message)
