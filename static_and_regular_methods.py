# -*- coding: utf-8 -*-

class Employee:
    #class variables can be used in all instances two ways, Employee.raise_amount or self.raise_amount
    raise_amount= 1.04
    num_of_emps=0
    def __init__(self,first,last,pay):
        self.first=first #possible option: self.fname=first
        self.last=last #optional: self.lname=last
        self.pay=pay
        self.email=first + '.' + last + '@company.com'
        #the following is a class variable which is constant for all instances, whereas if we write self it can be overriden by instances
        Employee.num_of_emps += 1
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    def apply_raise(self):
        #using class variable
        self.pay=int(self.pay * self.raise_amount)
    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount=amount
        
    @classmethod
    def from_string(cls,emp_str):
        first, last, pay=emp_str.split('-')
        return cls(first, last, pay)
    #creating static methods
    @staticmethod
    def is_workday(day):
        if day.weekday() ==5 or day.weekday() == 6:
            return False
        return True
#now we can create instances
emp_1=Employee('Corey','Schafer',50000)
emp_2=Employee('Test','User',60000)

#so after creating the class variable we can do the following

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)


#to change the raise amount,option 1, using classmethod
Employee.set_raise_amount(1.09)
#the above can be done like this too, option 2
Employee.raise_amount=1.09
#we can also do it using instances, option 3
emp_1.raise_amount=1.09

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)




#using class methods as constructors
emp_str_1='John-Doe-70000'
emp_str_2='Steve-Smith-90000'
emp_str_3='Jane-Doe-80000'
#this is class method as constructor
new_emp_1=Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)

#differences
'''
regular methods: pass self or instance as the firsst argument
class methods: pass cls or class as their first argument
static methods: does not pass anything automatically

'''
#static methods expalined here

import datetime
my_date=datetime.date(2022, 7, 1)
print(Employee.is_workday(my_date))







