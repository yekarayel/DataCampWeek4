"""Following is a preview of the numpy array x: 
np.array([10, 15, 22, 13, 17, 20, 8])

Select the code to return the output 
[10 15 13  8]

Select the code:

x_small = x[x < 13]         x_small = x[x < 17]         x_small = x[x == 15]
print(x_small)              print(x_small)              print(x_small)          """


x = np.array([10, 15, 22, 13, 17, 20, 8])
x_small = x[x < 17]
print(x_small)
