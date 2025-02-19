import pandas as pd
ser=pd.Series([20,30,10,40,50,70])
print("Original Data Series:")
print(ser)
new_ser = ser.sort_values(ascending=True).reset_index(drop=True)
print('After sort:')
print(new_ser)
