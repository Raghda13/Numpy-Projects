import numpy as np

var = np.loadtxt(r"C:\Users\Pc Store\Downloads\Lending-company-Numeric\Lending-company-Numeric.csv", delimiter=',' )
var
print(var)
#print(np.shape(var))

#print(np.reshape(var,[6,1043]))

# turn the rows into columns
#print(np.transpose(var))
#print(np.reshape(var,[2,3,1043])) # two 2d arrays OR 3d array and 3 rows in each one of them
# Load the data
var = np.genfromtxt(r"C:\Users\Pc Store\Downloads\Lending-company-Numeric\Lending-company-Numeric.csv",
                 delimiter=',',
                  skip_header = 1)

# Delete the 2nd and 4th column and print the resulting array without any nan values
print(np.delete(var, [1, 3], axis=1))


