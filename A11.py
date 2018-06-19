#creating a threading process which prints with a delay of five seconds
'''
importing the time and thread modules
'''

import time
from threading import Thread

def func1(tname):
         print(tname)
         print("you're inside the thread, sleep for 5 sec")
         time.sleep(5)
         '''
         this will cause a delay of five seconds
         '''
         print("ended")
tname = input("enter thread name")
t1 = Thread(target = func1, args=(tname,))
t1.start()


#printing numbers 1 to 10 with a second of delay each
import time
import threading
class num(threading.Thread):
                def __init__(self):
                            threading.Thread.__init__(self)
                def run(self):
                            for i in range (0,10):
                                     time.sleep(1)
                                     '''
                                     sleep for 1 sec after each step
                                     '''
                                     print(i)

t2 = num()
t2.start()


#print list elements at a multiplied interval of 2
import time
import threading

l= [1,2,3,4,5]

class newl(threading.Thread):
                def __init__(self):
                       threading.Thread.__init__(self)
                def run_newl(self):
                       for v in range(1,6):
                                       for w in l:
                                              print(w)
                                              time.sleep(v*2)
'''
each time, the sleep will be multiplied by 2
'''
t3 = newl()
t3.start

#factorial
import time
import threading

class fact(threading.Thread):
                 def __init__(self):
                         threading.Thread.__init__(self)
                 def run_fact(self):
                         f = 1
                         for r in range(1, n+1):
                                       f = f*r
                         print(f)
n = int(input("enter number for fact:"))
t4 = fact()
'''
the factorial will be calculated through the thread
'''
t4.start()

