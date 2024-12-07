import numpy as np


#Dot product


### Dot product: product of two arrays
f = np.array([1,2,3])
g = np.array([4,5,3])    # 1*4 + 2*5 + 3*6
print(np.dot(f, g))  # 23




#Matrix multiplication


h = [[1,2],[3,4]]
i = [[5,6],[7,8]]
### 1*5+2*7 = 19
print(np.matmul(h, i))


