import pandas as pd
#scatter empid empsal
#history empnam empsal
import matplotlib.pyplot as plt

empdata=[(101,"harsh",100000,"1-03-04"),
         (102,"jenish",150000,"1-03-04"),
         (103,"jeel",120000,"1-03-04"),
         (104,"het",105000,"1-03-04")]

print(empdata)

newdata=pd.DataFrame(empdata,columns=("empid","empname","empsal","empdob"))
print(newdata)
print(newdata[1:4])
print(newdata[4:0:-1])
print(newdata[newdata.empsal>110000])
df1=newdata.sort_values("empname",ascending=False)
print(df1)

# plt.scatter(newdata.empid,newdata.empsal,color="green",marker="^",linewidth=8,edgecolor="pink")
# plt.title ("scatter chart ",fontsize=40)
# plt.xlabel("empid")
# plt.ylabel("salry")

# plt.hist(newdata.empsal)
c=['red','green','pink','purple']
plt.pie(newdata.empsal,labels=newdata.empname,colors=c,shadow=True,startangle=90)








