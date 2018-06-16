#creating a base class animal and inheriting class tiger from it
class animal:
        eyes=2
        ears=2
        nose=1
        def animalattribute(self):
                          print("the animal has %d eyes" % self.eyes)
                          print("the animal has %d ears" % self.ears)
                          print("the animal has %d nose" % self.nose)
class tiger(animal):
        def __init__(self):
                       print("it's a tiger")
t = tiger()
t.animalattribute()

#display an output
"""
function A calls its own function g, while function B calls its own function g 
so, the outputs differ when we print f
A B
A B
"""

#displaying cops and their missions
class cop:
      def funct(self):
                   self.name = "lestrade"
                   self.age = 40
                   self.work_ex= 20
                   self.desig= "senior of"
      def update(self):
                   self.name = input('enter name of the cop')
                   self.age  = int(input('enter age'))
                   self.work_ex = int(input('enter the years of work experience'))
                   self.desig = input("enter the cop's designation")
      def display(self):
                   print(self.name)
                   print("age of the cop is %d" % self.age)
                   print("work experience is %d" % self.work_ex)
                   print(self.desig)
     
class mission(cop):
          def add_mission_details(self):
                   self.nam= "mission 1"
                   self.place = "new york"
                   self.funct()
                   self.display()
                   self.mdisplay()
                   p = int(input('enter 1 to update'))
                   if p == 1:
                         self.update()
                         self.nam = input("enter the name of mission")
                         self.place = input("enter the place ")
                         self.display()
                         self.mdisplay()
          def mdisplay(self):
                   print('mission details are')
                   print(self.nam)
                   print(self.place)

cop1 = mission()
cop1.add_mission_details()




#creating a base class shape and calculating areas of rectangle and square
class shape:
      def func(self):
                 self.l=int(input('enter length'))
                 self.b=int(input('enter breadth'))
      def area(self):
                 self.area = self.l*self.b
                 print("the area is %d" % self.area)
class square(shape):
      def __init__(self):
                print('enter dim for a square')
                self.func()
class rectangle(shape):
     def __init__(self):
                print('enter dim for a rectangle')
                self.func()
s = square()
s.area()
r = rectangle()
r.area()
