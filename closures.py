# -*- coding: utf-8 -*-

#lets start from the following example in order to uderstand closures

def outer_func():
    message = 'Hi'
    
    def inner_func():
        print(message)
    
    return inner_func()

outer_func()


'''
a closure is a func inside another func which remebers the variables of its outer_func, even 
after the outer func is already executed
'''

def outer_func():
    message = 'HI'
    
    def inner_func():
        print(message)
    
    return inner_func

my_func = outer_func()

hi_func = my_func()



def outer_func(msg):
    message = msg
    #message is also called free variable which closure remembers
    def inner_func():
        print(message)
    
    return inner_func

hi_func = outer_func('hi')
hello_func = outer_func('hello')

hi_func()
hello_func()



















