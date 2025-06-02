import matplotlib.pyplot as plt 

x =[1, 2, 3, 4, 5, 6, 7]
y =[1, 2, 1, 2, 1, 2, 1]

# creating error
x_error = 0.5
y_error = 0.3

# plotting graph
plt.plot(x, y)
plt.errorbar(x, y, 
             yerr = y_error, 
             xerr = x_error, 
             fmt ='o')