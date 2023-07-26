"""
wpp to calculate inhamd salary of employee based on their basic salary
1-hra is 50% of basic salary
2-da is 35% of basic salary
3-ta is 12% of basic salary
4-pf is 50% of basic salary
"""
emp_id=int(input("enter the employee id :"))
name=input("enter the employee name :")
designation=input("enter the designation :")
doj=input("enter the date of joining :")
basic_salary=float(input("enter the basic salary of employee :"))
hra=basic_salary*0.5
da=basic_salary*0.35
ta=basic_salary*0.12
pf=basic_salary*0.5

inhand_sal=basic_salary+hra+da+ta-pf
print("\n\nemployee id :",emp_id,"\nemployee name :",name,"\ndesignation :",designation,"\ndate of joining :",doj)
print("\nbasic salary: ",basic_salary)
print("\n+        hra:",hra)
print("\n+         da:",da)
print("\n+         ta:",ta)
print("\n       total:",basic_salary+hra+da+ta)
print("\n-         pf:",pf)
print("\ninhand salary",inhand_sal)
"""
input
empid 
name
designation
joining date
years of experience
basic salary
"""
