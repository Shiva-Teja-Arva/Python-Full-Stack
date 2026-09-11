import numpy as np
# Creation of 2-D Array
a = np.array([[1,2,3],[4,5,6]])
print(a)
print(type(a))
print(a.size) # gives the size of the array
print(a.shape) # gives the rows and cols
print(a.ndim)
print("="*60)
print("Reshaping the Array:")
print(a.reshape(3,2))
print("="*60)
print("Flattening the Array:")
print(a.flatten())
