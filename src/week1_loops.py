def trade_result(capital,profit):
	capital+=profit
	if p>0:
		print(f"Profit is: {profit},New Capital is:{capital}")
	else:
		print(f"Loss is: {profit},New Capital is:{capital}")
	return capital
capital=1000
profits=[50,-20,30,10,-40,60]

for p in profits:
	message=trade_result(capital,p)
	
