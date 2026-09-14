import matplotlib.pyplot as plt
cities = ["Hyderabad","Bengaluru","Vizag","Chennai"]
sales = [90000,200000,60000,70000]
plt.bar(cities,sales)
plt.title("Bar Chart Example \n Sales in Cities")
plt.xlabel("Cities")
plt.ylabel("Sales")
plt.show()