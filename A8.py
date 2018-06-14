#What is time tuple?
#Python stores time in tuples. These tuples are made up of nine numbers.
'''
Index                       Field
0                           year
1                           month
2                           day
3                           hour
4                           minute
5                           second
6                           day of week
7                           day of year
8                           DST

'''

#Printing the formatted time
import time
print('the formatted time is')
print(time.asctime())

#Extracting month from time
import datetime
d = datetime.date.today()
print("the month of today's date is")
print(d.month)

#Extracting day from time
y = time.localtime()
day = str(y.tm_day)
print("today the day is")
print(day)

#Print date
print('the date is')
print(d)


#getting the local time through dedicated func
print('The time using local time is')
print(time.localtime())

#calculating factorial through dedicated func
import math
x = int(input('Enter a num to calculate its factorial'))
f = math.factorial(x)
print(f)

#calculating GCD through dedicated function
a = int(input('enter first num fot gcd'))
b = int(input('enter second num for gcd'))
gcd = math.gcd(a,b)
print('greatest common divisor is')
print(gcd)

#using os package and its functions
import os
print("the current working directory is")
print(os.getcwd())
print('the current working environment path is')
print(os.environ.get('PATH'))
