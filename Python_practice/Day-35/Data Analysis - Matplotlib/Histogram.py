import matplotlib.pyplot as plt
ages = [10,14,14,15,18,19,20,13,14,16]
plt.hist(ages,bins=5)
plt.title("Histogram \n Ages - Frequency")
plt.xlabel("Ages")
plt.ylabel("Frequency")
plt.show()

