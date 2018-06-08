#working with tuples
#1
a = 1,2,3,6,8,5
print(a)
print(type(a))
print(len(a))

#2
print('largest elem of the tuple')
print(max(a))
print('smallest elem of tuple')
print(min(a))

#3
p = 1
for i in a: 
       p = p*i
print('The product of the tuple is')
print(p)

#working with sets
#1
print('enter the elements of the set1')
s1 = set([s1 for s1 in input().split()])
print('set1 is')
print(s1)
print('enter the elem of set2')
s2 = set([s2 for s2 in input().split()])
print('set2 is')
print(s2)


#2
s3 = s1 - s2
print('The difference of the two sets is')
print(s3)

#3
print('intersection of the two sets is')
print(s1 & s2)

#4
if(s1<=s2):
      print('s1 is smaller/subset of s2')
else:
   print('s2 is smaller/subset of s1') 

#working with Dictionaries 
print('enter credentials for 10 students')
dic = {}
for i in range(0,9):
         key = input('enter name of the std:')
         value = input('enter the marks of the std:')
         dic[key] = value
         print(dic)

#sorted according to the marks
print(sorted(dic.values()))
import operator
sort = sorted(dic.items(), key=operator.itemgetter(1))
print(sort)

#occurence of each letter in mississippi
h = ('mississippi')
print(h)
i = h.count('i')
m = h.count('m')
s = h.count('s')
p = h.count('p')
count_dict = {'M': m, 'I': i, 'S': s, 'P':p}
print(count_dict)
