# 9/8/23
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("IRIS.csv")

print(data)
# fig=plt.figure(figsize=(10,7)) #this fixes size of figure
c=["red",'green','pink']
plt.bar(data['species'],data['petal_length'],color="pink")
plt.bar(data['species'],data['petal_width'],color="red")
plt.bar(data['species'],data['sepal_length'],color="yellow")
plt.bar(data['species'],data['sepal_width'],color="blue")

plt.title("iris data",fontsize=20,color="blue")
plt.xlabel("species",fontsize=20,color="green")
plt.ylabel("sepal width",fontsize=20,color="green")
labels=['petal length','petal width',"sepal length","sepal width"]
plt.legend(labels)
plt.show()









