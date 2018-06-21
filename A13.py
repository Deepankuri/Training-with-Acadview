#Question1
"""
Handling a zero divion exception.
Since a number divided by zero is undefined, it will
print "undefined inputs"
"""
try:
	a=3
	if a<4:
		a=a/(a-3)
except ZeroDivisionError:
	print("undefined inputs")

#Question2
"""
Handling an index error when element is not present for a
particulr index.

"""
x = int(input("enter index to print element"))
try:
	l = [1,2,3]
	print(l[x])
except IndexError:
	print("please enter a valid index!")

#Question3
try:
    raise NameError("Hi there")  # Raise Error
except NameError:
    print ("An exception")
    raise  # To determine whether the exception was raised or not
"""
Output would be:
An exception
Traceback (most recent call last):
  File "C:\Program Files\Sublime Text 3\new3.py", line 2, in <module>
    raise NameError("Hi there")  
NameError: Hi there

It is so because since we're raising an error on our own, we get the statement "an exception"
and since the statement "hi there" is attached to the exception, it will get printed 
everytime this exception is raised 
"""

#Question4
# Function which returns a/b
def AbyB(a , b):
	try:
		c = ((a+b) / (a-b))
	except ZeroDivisionError:
		print("a/b results in 0")
	else:
		print(c)

# Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)
"""
Output would be:
-5.0
a/b result in 0

It is so because everytime the try block runs successfully,
the else statement would print, otherwise an exception would be raised
and it'd print the exception error
"""

#Question5
"""
Import error is when we try to import some library or module that doesn't exist 
or when we import something from a module that it doesn't even contain.
"""
try: 
	import dee
except ImportError:
    print('import errorhas occured, since no such library exists')

"""
Value error is when a built in operation or function has the right data type
but carries the wrong value
"""
try:
	t = int(input('enter'))
	print(t)
except ValueError:
	print("it's a value error, please enter valid value")

"""
Index error is when we try to search for an index for which the element 
doen't exist in out data.
"""
x = int(input("enter index to print element"))
try:
	l = ['deepankuri', 'ram','prateek']
	print(l[x])
except IndexError:
	print("please enter a valid index!")

#Question6
"""
we'll take the input of age and check it, if it is greater than 18 or not.
For ages smaller than 18, we'll get an error saying that the age is too small.
Age too small error is an error that we've raisd by oueselves.
"""
class AgeTooSmallError:
	pass
def ip():
	try:
		age = int(input("enter age"))
	except AgeTooSmallError:
		raise AgeTooSmallError
	if age<18:
		print("please enter a valid age, i.e. above 18")
		continue
ip()

