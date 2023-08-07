import pandas as pd
import numpy as np
data=pd.read_csv("")
#print(data)
#print(data.shape) #for find total row and column
print(data.columns)
#data=data.head(30)
#print("null record in gender",data["Gender"].isna().son())
# print(data.isnull())
# new_data=pd.notnull(data['Gender'])
# print(data[new_data])
print(data['Gender'].fillna("no gender ",inplace=True)) #replace null gender into no gender
print("null record in gender",data["Gender"].isna().sum())

print(data['Firstname'].fillna("no name"),inplace=True)
print("null record in first name",data["Firstname"].isna().sum())

print("null record in start date",data["startdate"].isna().sum())
print("null record in last login time",data["last login time"].isna().sum())

print("null record in salary",data["salary"].isna().sum())
print("null record in bolus %",data["Bonus %"].isna().sum())

print(data["senior Management"].fillna("no management",inplace=True))
print("null record in senior Management",data["Senior Management"].isna().sum())

print(data["Team"].fillna("no team",inplace=True))
print("null record Team",data["Team"].isna().sum())









