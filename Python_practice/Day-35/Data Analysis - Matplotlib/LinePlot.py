import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[10,20,60,40]
plt.plot(x,y,marker="s",color="red",linestyle="--")
plt.title("Line-Plot Example")
plt.xlabel("x-data")
plt.ylabel("y-data")
plt.grid(True)
plt.show()
