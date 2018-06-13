#area of circle
r = int(input('enter radius'))
def area(a):
 return(3.14*a*a)
ar = area(r)
print('area of circle is')
print(ar)

#perfect number
def perfect():
      for num in range(1,1000):
                   sum = 0
                   for n in range(1, num-1):
                               if (num%n == 0):
                                        sum = sum+n
                   if (sum == num):
                          print(num)
                          print('is a perfect number')
perfect()

#table of 12
def mul(x, y=1): 
      print(x*y)
      if y !=10:
            mul(x,y+1)
mul(12)

#power function
def pow(p,q):
        if q == 1:
              return p
        else:
           return p * pow(p,q-1)
p = int(input('enter base number'))
q = int(input('enter number for power'))
power = pow(p,q)
print(power)

#factorials and numbers dictionary
def fact(f):
       if f == 0 or f == 1:
             return 1
       else:
          return f*fact(f-1)
dict = {}
for j in range(0,10):
         j = int(input('enter any num for factorial'))
         dict[j] = fact(j)
print(dict)
