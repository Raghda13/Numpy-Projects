import numpy as np
var = np.genfromtxt(r"C:\Users\Pc Store\Downloads\Lending-company-Numeric-NAN\Lending-company-Numeric-NAN.csv"
        ,delimiter=';')
print(var.astype(dtype=np.int32))



