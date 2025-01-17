print("This program will use numpy array to create a series ")
import pandas as pd
import numpy as np
numarr=np.arange(1,20,1)
series=pd.Series(numarr**2, index=numarr*2)
print(series)
