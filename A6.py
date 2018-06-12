#Print int from user
for i in range(0,10):
          x = int(input('enter an integer'))
          print(x)

#Infinite loop
a = 1
while(a>0):
     print('infinite loop')



#lists of integer and their squared values
l1 = []
for j in range(0,10):
       n = int(input('enter integers'))
       l1.append(n)
print(l1)

l2 = []
for m in l1:
      s=m*m
      l2.append(s)
print(l2)

#Separate lists acc to data types
li = [1,2,3,4,'dee','ash',2.3,5.6,8.9,9,7]
floatl = []
strl = []
intl = []
for k in range(len(li)):
         if type(li[k])==float:
                   floatl.append(li[k])
         if type(li[k])==str:
                   strl.append(li[k])
         if type(li[k])==int:
                   intl.append(li[k])
print(floatl)
print(stringl)
print(intl)


#even and odd
even = []
odd = []
for q in range(1,101):
        if (q%2==0):
               even.append(q)
        else:
           odd.append(q)
print(odd)
print(even) 

#Pattern
for e in range(0,5):
      for f in range(0,e+1):
                  print('*' , end=" ")
      print('\n')

#user def dict
dict = {}
print("enter the dictionary")
for v in range(0,10):
         v = input("enter key")
         dict[v] = int(input('enter corresponding value'))
print('the dictionary is')
print(dict)

#enter and delete a list
newlist = []
for z in range(0,10):
             w = int(input('enter int elem for list'))
             newlist.append(w)
u = int(input('enter elem to search and delete'))
newlist.remove(u)
print(newlist)
