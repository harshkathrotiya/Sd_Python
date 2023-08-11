
#area plot
import plotly.express as ps
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# 11/08/23
# data=pd.read_csv("IRIS.csv")
df=ps.data.iris()

# print(data)
# l=(int(data['sepal_width']), int(data['sepal_length']),int(data['petal_width']))
plt.stackplot(df['sepal_width'],df['sepal_length'],df["petal_width"],data=df,colors=['red','green'])
# ran1=np.random.randint(0,10,50)
# ran2=np.random.randint(0,20,50)
# ran3=np.random.randint(0,20,50)
# plt.stackplot(ran1,ran2,ran3)







