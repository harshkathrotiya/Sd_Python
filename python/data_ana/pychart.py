# 9/8/23

import matplotlib.pyplot as plt
fruits=['apple','cherry','grapes','papaya']
frequency=[4,6,10,16]

c=['red','green','pink','purple']
plt.figure(figsize=(10,10),facecolor="grey")
explode=[0,0.0,0.3,0.1]
wp={'linewidth':2,'edgecolor':'green'}
plt.pie(frequency,labels=fruits,colors=c,shadow=True,explode=explode,startangle=90,wedgeprops=wp)
plt.title("fruits pie chart",color="red",fontsize=25)
plt.legend(fruits,loc="upper right")
plt.show()