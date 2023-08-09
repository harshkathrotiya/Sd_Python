# 9/8/23
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data=pd.read_csv('IRIS.csv')
print(data)
fig=plt.figure(figsize=(10,7))
#figure size
barwidth=0.5
fig,ax=plt.subplots(figsize=(16,9))
br1=np.arange(len(data["species"]))
br2=[x+50*barwidth for x in br1]
br3=[x+50*barwidth for x in br2]
br4=[x+50*barwidth for x in br3]
plt.bar(br1,data['sepal_length'],color='red')
plt.bar(br2,data['sepal_width'],color="pink")
plt.bar(br3,data['petal_width'],color="grey")
plt.bar(br4,data['petal_length'],color="black")
plt.title("bar chart",fontsize=20,color="blue")
plt.xlabel("species", fontsize=20,color="green")
plt.ylabel("sepal length", fontsize=20,color="green")
labels=['sepal length','sepal width','petal width','petal length']
plt.xticks([r+50 *barwidth for r in range(len(data['species']))],labels)
plt.legened(labels)
plt.show()




