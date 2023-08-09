# two type of data:qualitative,quantitative
#bar chart:x axes categerogical value ,y axes frequency
#histogram :x axes numerical and continuous means range ,y axes frequencyy.
# 9/8/23
import matplotlib.pyplot as plt
fruits=['apple','cherry','grapes',"papaya"]
frequency=[4,6,10,16]
c=["red","green","pink","purple"]
# plt.bar(fruits,frequency,color=c)
plt.barh(fruits,frequency,color=c)
plt.title("Bar Chart", fontsize=20,color="blue")
plt.xlabel("fruits")
plt.ylabel("frequency", )
plt.show()
















