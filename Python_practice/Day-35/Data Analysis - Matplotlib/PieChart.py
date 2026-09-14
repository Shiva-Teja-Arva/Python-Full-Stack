import matplotlib.pyplot as plt
fruits = ["Apple","Banana","Mango","Grapes"]
percentages = [35,20,15,30]
plt.pie(percentages,labels = fruits,autopct = "%1.1f%%")
plt.grid(True)
plt.title("Pie-Chart Example \n Fruits-Percentage")
plt.show()
