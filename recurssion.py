# -*- coding: utf-8 -*-

#recursion means calling a function inside itself or a function calling itself

i=0

def greet():
    global i
    i+=1
    print('Hello',i)
    greet()
    
greet()


#by default recursion limit is 3000 but we can change it using the sys module

import sys

print(sys.getrecursionlimit())

#we can change the limit as below
sys.setrecursionlimit(4000)



#factorial

def fact(n):
    if n==0:
        return 1
    #it will keep calling itself until the n is equal to 0
    return n*fact(n-1)

print(fact(5))









