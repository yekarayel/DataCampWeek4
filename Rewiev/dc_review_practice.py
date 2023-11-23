"""Complete the code to return the output 
import numpy as np
np_arr1 = np.array([1,2,3,4])
np_arr2 = np.array([5,6,7,8])
print(
((np_arr1, np_arr2)))
[[1 5]
 [2 6]
 [3 7]
 [4 8]]
 
 Fill in the blanks
 * np.column_stack      * np.column     * np.row_stack      * np.row   """

import numpy as np
np_arr1 = np.array([1,2,3,4])
np_arr2 = np.array([5,6,7,8])
print(np.column_stack((np_arr1, np_arr2)))
