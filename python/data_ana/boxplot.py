#11/08/23
#box plot or five number plot 
# 1.q1,2.q2.3.q3,4.interquartilerange(iqr),5.range
# if the probability of nuber of number is same of the set of num is randon number
import numpy as np
import matplotlib.pyplot as plt

#dataset
np.random.seed(10)
data1=np.random.normal(0,10,100)
data2=np.random.normal(0,20,50)
data=[data1,data2]
c=['pink','green']
print(data)
plt.boxplot(data,vert=0)
plt.show()
