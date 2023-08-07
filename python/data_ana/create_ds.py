import pandas as pd
import numpy as np

dict={'first score':[100,90,np.nan,95],
      'second score':[30,45,56,np.nan],
      'third score ':[np.nan,40,80,98]
      }
#creating dataframe from the list
df=pd.DataFrame(dict)
#using isnull() function
print("is null ...",df.isnull())

#filling missing value using filla()
print("fillna (0).....",df.fillna(0))

#filling a missing value with previous ones
print("pad........",df.fillna(method='pad'))

#filling null value using fillna function usefor backward
print("bfill...",df.fillna(method='bfill'))

#to interploate the missing values
print("inerploate ...",df.interpolate(method='linear',limit_direction='forward'))

#using dropna()function remove all ro where null
print("dropna ...",df.dropna())

#drop a columns which have at least 1 missingvalues only remove column
print("dropa....",df.dropna(axis=1))

