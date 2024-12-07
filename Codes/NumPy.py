# NumPy provides a high-performance multidimensional array object, and tools for working with arrays.





#importing numpy as np
import numpy as np



#changing python list into int numpy array

list= [6,9,6,9]
print(type(list))

numpy_array= np.array(list)
print(type(numpy_array))



#changing python list into float numpy array

   
python_list = [1,2,3,4,5]

numpy_array = np.array(python_list, dtype=float)
print(numpy_array)


#creating boolean numpy arrays
numpy_bool_array = np.array([0, 1, -1, 0, 0], dtype=bool)
print(numpy_bool_array) # array([False,  True,  True, False, False])




#Creating multidimensional array using numpy
two_dimensional_list = [[0,1,2], [3,4,5], [6,7,8]]
numpy_two_dimensional_list = np.array(two_dimensional_list)
print(type (numpy_two_dimensional_list))
print(numpy_two_dimensional_list)







# We can always convert an array back to a python list using tolist().
np_to_list = numpy_array_from_list.tolist()
print(type (np_to_list))
print('one dimensional array:', np_to_list)
print('two dimensional array: ', numpy_two_dimensional_list.tolist())




