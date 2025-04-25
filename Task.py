import numpy as np
np.set_printoptions(suppress=True,linewidth=100,precision=2)
raw_data=np.genfromtxt(r"C:\Users\Pc Store\Downloads\EUR-USD Exchange Rate 2015\EUR-USD.csv"
                       ,delimiter=';')
print(raw_data)
# checking for incomplete data
print(np.isnan(raw_data).sum())



