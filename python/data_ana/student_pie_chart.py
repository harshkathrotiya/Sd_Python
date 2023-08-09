# 9/8/23
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("student.csv")

print(data)
plt.figure(figsize=(20,20),facecolor="#8CABFF")
exp=[0,0.1,0,0.4,0.3,0,0,0]
plt.pie(data['percentage'],labels=data['student_name'],shadow=True,explode=exp)
plt.legend(data['student_name'])
plt.title("student percentages pie chart",color="orange",fontsize=70)
plt.show()
