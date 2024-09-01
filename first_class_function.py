# -*- coding: utf-8 -*-
'''
first class func concept means that funcs can be treated like other objects


First-class Function A programming language is said to have First-class functions when
 functions in that language are treated like any other variable. For example, in such a
 language, a function can be passed as an argument to other functions, can be returned by 
 another function and can be assigned as a value to a variable.
'''


def square(x):
    return x*x


f=square(5)

print(square)
print(f)

#in the following we do

f=square

print(square)
print(f)
print(f(5))


#lets build the map func from scratch, which is Higher-order Function
#higher order funcs take one or more funcs as arguments

def my_map(func,arg_list):
    result= []
    for i in arg_list:
        result.append(func(i))
    return result

squares = my_map(square, [1,2,3,4,5])

print(squares)


def cube(x):
    return x*x*x

squares = my_map(cube, [1,2,3,4,5])

print(squares)


def logger(msg):
    
    def log_message():
        
        print('Log:',msg)
    #so we return log_message func, we dont put parenthesis since it should not be executed right away
    return log_message

log_hi = logger('Hi!')
log_hi() #now it is as if, log_message func


#usage of the above funcs

def html_tag(tag):
    
    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag,msg))
    return wrap_text

print_h1 = html_tag('h1')
print_h1('Test Headline!')
print_h1('Another headline')





