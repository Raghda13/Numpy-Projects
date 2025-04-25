import numpy as np
var = np.genfromtxt(r"C:\Users\Pc Store\Downloads\Lending-company-Numeric-NAN\Lending-company-Numeric-NAN.csv",
        delimiter=';')
var
print(var)
temporary_mean=np.nanmean(var,axis=0).round(2)
print(temporary_mean)
# check the mean of the first column
print(temporary_mean[0])
# find the average value of the first column
print(np.mean(var[:,0]).round(2))




