# #13-1

# class Student:
#     def __init__(self):
#         pass
#         self.total
#     def marks(self):
#         id=int(input("enter your roll no :"))
#         name=input("eneter your name :")
#         marks1=float(input("enter your marks :"))
#         marks2=float(input("enter your marks 2 :"))
#         marks3=float(input("enter your marks 3 :"))
#         marks4=float(input("enter your marks 4 :"))
#         marks5=float(input("enter your marks 5 :"))
#         marks6=float(input("enter your marks 6 :"))
#         per=marks1+marks2+marks3+marks4+marks5+marks6
#         self.total=per/6
# class Faculty(Student):
#             def __init__(self):
#                   super().__init__(self,Student.total)
#                   self.total=Student.total
#             def grade(self):
#                 if self.total <=33:
#                       print("fail")
#                 elif self.total>=33 and self.total<=50:
#                      print("grade:c")
#                 elif self.total>=50 and self.total<=60:
#                      print("grade:c+")
#                 elif self.total>=60 and self.total<=70:
#                       print("grade:b")
#                 elif self.total>=70 and self.total<=80:
#                       print("grade:b+")
#                 elif self.total>=80 and self.total<=90:
#                      print("grade:a")
#                 elif self.total>=90 and self.total<=100:
#                       print("grade:a+")
#                 else :
#                      print("marks are not valid")

# fac=Faculty()
# fac.marks()
# fac.grade()
            

# write a progaram to make two classes named student and faculty make a method to enter the student details inside student
#class.create a one method inside faculty class to read the student data and calculate the student total marks.
# based on total marks faculty gives the grade.grades must be visible to students.

class Student:
    def __init__(self,stu_no,stu_name):
        self.stu_no=stu_no
        self.stu_name=stu_name
        
    def display(self,grade):
        self.grade=grade
        print("student no : ",self.stu_name)
        print("name is :",self.stu_no)
        print("grade is  :",self.grade)
class faculty:
    def __init__(self,sub1,sub2):
        self.sub1=sub1
        self.sub2=sub2
    def cal_grade(self):
        self.total=0
        self.grade=""
        self.total=self.sub1+self.sub2
        if self.total>=100 and self.total <200:
            self.grade="pass"
            return self.grade
        else :
            self.grade="fail"
            return self.grade
stu=Student(1,"abc")
fac=faculty(50,100)
result=fac.cal_grade()
stu.display(result)
