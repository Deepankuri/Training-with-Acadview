#Leap year
y =int(input("enter the year"))
print(y)

if ( y%4==0 and y%100!=0 or y%400==0 ):
                           print('leap year')
else:
   print('not a leap year')

#Take input for length and breadth and check for circle or square
l = int(input('enter the length:'))
b = int(input('enter the breadth:'))

if (l == b):
        print("it's a square")
else:
   print("it's a rectangle")

#oldest and youngest of the three people
x = int(input('enter the age of first person'))
y = int(input('enter the age of second person'))
z = int(input('enter the age of third person'))

if(x>y):
    if(x>z):
       print("x is the oldest person")
    else:
       print("z is the oldest ")

elif(y>z):
       print('y is the oldest')

elif(z>y):
       print('z is the oldest')

if(x<y):
     if(x<z):
       print("x is youngest")
     else:
       print("z is youngest")
elif(y<z):
       print('y is youngest')

elif(z<y):
       print('z is youngest')

#Displaying the prize won
pr = int(input("enter the participant's score"))

if (pr<=200):
         if (pr>1 and pr<=50):
                   print("sorry, no prize this time")
         elif (pr>=51 and pr<=150):
                   print("congratulations! you won a wooden dog")
         elif(pr>=151 and pr<=180):
                   print("congrats! you've won a book")
         elif(pr>=181 and pr<=200):
                   print("congrats! you won chocolates")
else:
   print('please enter valid scores')

#Question 5
q = int(input("enter the quantity of products purchased: "))
p = q*100

if p>1000:
     new_p = p - p*0.1
     print("congrats! you get a discount, and now your payable amount is: ")
     print(new_p)
else:
     print("your payable amount is")
     print(p)
