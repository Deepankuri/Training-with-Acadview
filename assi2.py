'''
Create two sorted arrays and merge them into another sorted array
'''
a = [5, 19, 10]
print(a)
a.sort()
print(a)
b = [6, 13, 4]
print(b)
b.sort()
print(b)
c = a + b
print(c)
c.sort()
print(c)

'''
implementing stack
'''

s = [1,2,5,4]
print('the stack is \n')
print(s)
print('adding new element 8 to stack')
s.append(8)
print(s)
print('last element will be deleted by lifo')
print(s.pop())
print(s)

'''
implementing queue
'''
q = [7, 10, 15]
print('queue is \n')
print(q)
print('adding new elem  10 to q')
q.append(10)
print('first elem deleted by fifo')
print(q.pop(0))
print(q)
