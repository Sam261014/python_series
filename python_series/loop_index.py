print("This program will create a series using range and loop values \n\n")
import pandas as pd
ser=pd.Series(range(5,30,5), index=[x for x in 'abcde'])
print(ser)
