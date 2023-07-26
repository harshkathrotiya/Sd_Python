#wpp to enter student name,student rollno and any theree sub marks out of 100
#calculate the percentage of student and print the grade according to the given rule
#1) if percentage is less than 50 grade ff fail
#2) if between 50 to 60 cc 
#3) if 60 to 70 bc
#4)if 70 to 80 bb
#5)80 to 90 ab
#90 to 100 aa

name=input("plz enter your name :")
rol=int(input("enter your rollno :"))
s1=int(input("enter mark of subject1 :"))
s2=int(input("enter mark of subject2 :"))
s3=int(input("enter mark of subject3 :"))
per=(s1+s2+s3)/3
print("percentage =",per)
if per<50:
    print("grade :ff")
elif per>=50 and per<60:
    print("grade :cc")
elif per>=60 and per<70:
    print("grade :bc")
elif per>=70 and per<80:
    print("grade :bb")
elif per>=80 and per<90:
    print("grade :ab")
elif per>=90 and per<100:
    print("grade :AA")
else :
    print("enter valid value")
    
