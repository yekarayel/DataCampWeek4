"""Loop over NumPy array
If you're dealing with a 1D NumPy array, looping over all elements can be as simple as:

for x in my_array :
    ...
If you're dealing with a 2D NumPy array, it's more complicated. A 2D array is built up of multiple 1D arrays. 
To explicitly iterate over all separate elements of a multi-dimensional array, you'll need this syntax:

for x in np.nditer(my_array) :
    ...
Two NumPy arrays that you might recognize from the intro course are available in your Python session: np_height,
a NumPy array containing the heights of Major League Baseball players, and np_baseball, a 2D NumPy array that 
contains both the heights (first column) and weights (second column) of those players.

Instructions

* Import the numpy package under the local alias np.
* Write a for loop that iterates over all elements in np_height and prints out "x inches" for each element, 
where x is the value in the array.
* Write a for loop that visits every element of the np_baseball array and prints it out."""

# Import numpy as np
import numpy as np
## import pandas as pd
## np_baseball= pd.read_csv('baseball.csv')
## np_height= pd.read_csv('baseball.csv', index_col=4)


# For loop over np_height
for i in np_height:
    print("{} inches".format(i))

# For loop over np_baseball
for i in np.nditer(np_baseball):
    print(i)
