import numpy as np

array_A = np.array([[-2, 1, 0], [6, -3, 0], [-4, -6, -1]])
array_B = np.array([[-3, 2, 1], [1, -1, 0], [-3, 4, 5]])
  #  Combine the arrays to get the maximum values: Create a new array, combined_array

combined_array = np.maximum(array_A, array_B)
print(combined_array)
 #Calculate peak-to-peak differences for each column: For each column in combined_array
print(np.ptp(combined_array, axis = 0))