import pandas as pd
import matplotlib.pyplot as plt
    
def scat(a,b):
    plt.scatter(a, b,linewidths=8,edgecolors="pink")
    
def historigram(a):
    plt.hist(a)
    
def piechart(c,d):
    plt.pie(c,labels=d,shadow=True,startangle=90)    