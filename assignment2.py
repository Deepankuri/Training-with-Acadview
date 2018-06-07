'''
List with user defined inputs
'''
a = [a for a in input().split()]  
print(a)
'''
Adding two lists
'''
b = ['google', 'apple', 'facebook', 'microsoft', 'tesla']
print(type(a))
print(type(b))
c = a + b
print(c)
'''
Counting the number of times a particular object occurs in the list
'''
x = [1, 2, 3 , 1, 5, 1]
print(x)
print('count of appearances of 1 is \n ')
print(x.count(1))
'''
Creating and sorting a list of numbers
'''
y = [5, 9, 6, 3, 7]
print(y)
print('sorted list is')
y.sort()
print(y)
