g##What is numpy?
# -> its a module which we use for array it;s more faster and took less space

import numpy as np

a=np.array([1,2,3,4])
print(a)
 

#creating 2d array
b=np.array([(1,2,3,4),(5,6,8,2)])
print(b)
print(b.ndim)     #it will print the dimensions
print(b.itemsize) #getting the size of array
print(b.dtype)    #getting the data type
print(b.size)     #getting thesize of array (depend of dim)
print(b.shape)    #shape of  (2 row 4 column) 

# #we can also reshape the array (row and column)
# re=b.reshape(4,2)
# print(re)

