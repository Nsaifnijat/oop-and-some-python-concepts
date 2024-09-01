# -*- coding: utf-8 -*-


def decorator_function(original_function):
    def wrapper_function():
        return original_function()
    
    return wrapper_function


def display():
    print('display function ran')
    
decorated_display = decorator_function(display)

decorated_display()

#so the following shows the usage of decorators, where we add something to the output, without changing original func

def decorator_function(original_function):
    #def wrapper_function():*args and **kwargs means it can take any number of arguments
    def wrapper_function(*args,**kwargs):
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function(*args, **kwargs)
    
    return wrapper_function


@decorator_function
def display():
    print('display function ran')
    
display()

#the above is as like following
def display():
    print('display function ran')
    
display=decorator_function(display)
display()



#another func with arguments with same decorator,so we need to add arguments to our decorator 
@decorator_function
def display_info(name,age):
    print('display_info ran iwth arguments ({}, {})'.format(name,age))

display_info('John', 25)


#we can also create a class decorator

class decorator_class(object):
    
    def __init___(self, original_function):
        
        self.original_function = original_function
        
    def __call__(self, *args, **kwargs):
        print('wrapper executed this before {}'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)


@decorator_class
def display():
    print('display function ran')
    
display()

@decorator_class
def display_info(name,age):
    print('display_info ran iwth arguments ({}, {})'.format(name,age))

display_info('John', 25)




#practical examples for decorators

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)
    
    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)
    return wrapper


@my_logger
def display_info(name,age):
    print('display_info ran iwth arguments ({}, {})'.format(name,age))

display_info('Hank', 30)


#another example

def my_timer(orig_func):
    import time    
    def wrapper(*args, **kwargs):
        t1= time.time()
        result= orig_func(*args,**kwargs)
        t2 = time.time()-t1
        print('{} Ran in: {} sec'.format(orig_func.__name__,t2))
        return result
    return wrapper


@my_timer
def display_info(name,age):
    import time
    time.sleep(1)
    print('display_info ran iwth arguments ({}, {})'.format(name,age))

display_info('Hank', 30)




#now lets use stacked decorators


@my_logger #this means, display_info = my_logger(my_timer(display_info))
@my_timer
def display_info(name,age):
    import time
    time.sleep(1)
    print('display_info ran iwth arguments ({}, {})'.format(name,age))

print(display_info.__name__) #this returns wrapper and it gets passed to my_logger decorator
                            # but we want the display to be passed to the my_logger decorator, for this we use functools
display_info('Hank', 30)





from functools import wraps

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)
    
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)
    return wrapper



def my_timer(orig_func):
    import time  
    
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1= time.time()
        result= orig_func(*args,**kwargs)
        t2 = time.time()-t1
        print('{} Ran in: {} sec'.format(orig_func.__name__,t2))
        return result
    return wrapper

@my_logger
@my_timer
def display_info(name,age):
    import time
    time.sleep(1)
    print('display_info ran iwth arguments ({}, {})'.format(name,age))

print(display_info.__name__)
display_info('Hank', 30)















