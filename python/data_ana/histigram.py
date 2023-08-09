# 9/8/23
#histigram

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data=pd.read_csv("IRIS.csv")
print(data)
nbins=5
c=['red','blue','pink','green','yellow','sky']
plt.hist(data['sepal_length'],color=c[0],bins=nbins)
plt.hist(data['petal_length'],color=c[1],bins=nbins)
plt.title("histigram",fontsize=20,color="blue")
plt.xlabel("sepal length range", fontsize=20,color="green")
plt.ylabel("frequency", fontsize=20,color="green")

plt.show()

