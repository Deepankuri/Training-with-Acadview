#Creating a circle, initializing it, and calculating various attributes
class circle:
        def __init__(self):
                   self.t = int(input('enter radius of the circle'))
        def getarea(self):
                   area = 3.14*self.t*self.t
                   print('area of the circle is')
                   print(area)
        def getcircumfrance(self):
                   c= 2*3.14*self.t
                   print('circumfrance is')
                   print(c)
ob = circle()
ob.getarea()
ob.getcircumfrance()

#Creating a class for students, iitializing and displaying the details of each of the students
class stud:
         def __init__(self):
                   self.n = str(input('enter the name of the student'))
                   self.r = int(input("enter roll no of the student"))
         def disp(self):
                    print('name:')
                    print(self.n)
                    print('roll no:')
                    print(self.r)
std1 = stud()
std1.disp()
std2 = stud()
std2.disp()
std3 = stud()
std3.disp()
std4 = stud()
std4.disp()
std5 = stud()
std5.disp()

#Converting temperature to farenhiet or celsius
class temp:
       def __init__(self):
                 self.temp = int(input('enter the temperature'))
       def convertfarenhiet(self):
                  return (self.temp*(9/5))+32
       def convertcelcius(self):
                  return (self.temp-32)*(5/9)
v = int(input("enter 1 to convert c to f and 0 to convert f to c"))
obj = temp()
if v == 1:
      print('temp in faren is')
      print(obj.convertcelcius())
else:
    print('temp in celcius is')
    print(obj.convertfarenhiet())

#Creating a class for movie details and updating it
class movie:
       def __init__(self):
               self.g = input("movie name:")
               self.h = input("artist:")
               self.i = int(input("year:"))
               self.j = int(input("ratings:"))
       def display(self):
                print (self.g)
                print (self.h)
                print (self.i)
                print (self.j)
m1 = movie()
print(m1.display())
w = int(input("enter 1 to update previous movie and info, else enter 0"))

if w == 1:
      m2 = movie()
      print(m2.display())

#Creating a class for expenditure
class expend:
         def __init__(self):
                    self.ex = int(input("enter total expenditure"))
                    self.sav = int(input("enter total savings"))
         def display(self):
                    print("expenditure is:")
                    print(self.ex)
                    print("savings are:")
                    print(self.sav)
         def total(self):
                    self.total = self.ex + self.sav
                    print('total salary is')
                    print(self.total)
e1 = expend()
e1.display()
e1.total()
