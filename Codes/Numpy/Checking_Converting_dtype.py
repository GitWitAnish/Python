
import numpy as np

#Checking data types in Numpy

numpy_int_arr = np.array([1,2,3,4])
numpy_float_arr = np.array([1.1, 2.0,3.2])
numpy_bool_arr = np.array([-3, -2, 0, 1,2,3], dtype='bool')

print(numpy_int_arr.dtype)         #int
print(numpy_float_arr.dtype)       #float
print(numpy_bool_arr.dtype)        #boolean





#Converting data type in NUmpy

#Int to float
float = np.array([1,2,3,4], dtype = 'float')
print(float)



#float to int
int = np.array([1.,2.,3.,4.], dtype = 'int')
print(int)


#Int to bool
np.array([-3, -2, 0, 1,2,3], dtype='bool')

