#11/08/11
#scatter chart with regression
from sklearn import linear_model 
import matplotlib.pyplot as plt
import pandas as pd

x=[10,20,15,34,56,12,45]#IT'S compulsory that x and y have same number of the vlaues
y=[8,34,67,34,456,34,65]
data=pd.read_csv("Book1.csv")
# data=pd.DataFrame(x,y)
print(data)
res=data['height'].corr(data['weight'])
print("correlation is :",res)
if res<1 and res>0:
    print(res, "shows negative correlation ")
elif res>1:
    print(res,"shows positive correlation")
else :
    print("no correlation")
plt.scatter(data['height'],data['weight'],color="green",marker="^",linewidth=8,edgecolor="pink")
plt.title("scatter chart",fontsize=20)
plt.xlabel("height")
plt.ylabel("weight") 
# plt.plot(x,y)
# res=data.corr()
# print(res)
