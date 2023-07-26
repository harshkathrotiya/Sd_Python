#10 wpp to print sum of numbers present insight list
d=[]
sum=0
num=int(input("how many data you enter:"))
for i in range(num):
    dt=int(input("enter the data :"))
    d.append(dt)
    sum+=d[i]
print(d)
print("\n sum is :",sum)
#eval function is use when directly full list enter in one time.
l1=eval(input("enter list"))
sm=0
for i in l1:
    sm+=i
print("sum is :",sm)
