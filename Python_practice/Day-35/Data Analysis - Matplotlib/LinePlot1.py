import matplotlib.pyplot as plt

months = ["Jan","Feb","Mar","Apr"]
expenditures = [1000,3000,5000,4000]
incomes= [3000,6000,1000,5000]
# Drawing the Line Plot
plt.plot(months,expenditures,label= 'expenditure')
plt.plot(months,incomes,label = 'income')
plt.title("Line-Plot Example \n Month-wise incomes and expenditures")
plt.xlabel("Months")
plt.ylabel("Income-Expenditure")
plt.legend()
plt.grid(True)
plt.show()