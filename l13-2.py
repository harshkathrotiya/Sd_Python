# crete base class shape having two methods take sides and display sides and create a derived class rectangle 
#having find area method which uses    sites entered in shape class use inheritance to calculate the area of rectangle.

class Shape:
    def __init__(self,no_sides) -> None:
        self.no_sides=no_sides
        self.sides=[]
    def take_sides(self):
        for i in range(self.no_sides):
            self.s=float(input("enter value of sides :"))
            self.sides.append(self.s)
    def display_sides(self):
        for i in range(0,len(self.sides)):
            print("side",i+1,"is",self.sides[i])
class Rectangle(Shape):
    def __init__(self,num):
        Shape.__init__(self,num)
    def cal_area(self):
        a=self.sides[0]
        b=self.sides[1]
        area=a*b
        print("area is :",area)
rec=Rectangle(2)
rec.take_sides()
rec.display_sides()
rec.cal_area()