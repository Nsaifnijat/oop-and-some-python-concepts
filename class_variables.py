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
        #the following is a class variable which is constant for all instances,
        #whereas if we write self instead of Employee it can be overriden by instances
        Employee.num_of_emps += 1
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    def apply_raise(self):
        #without class variable
        #self.pay=int(self.pay * 1.04)
        #using class variable
        self.pay=int(self.pay * self.raise_amount)

#now we can create instances
emp_1=Employee('Corey','Schafer',50000)
emp_2=Employee('Test','User',60000)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

#so after creating the class variable we can do the following

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

#print namespace, or what it has inside
print(emp_1.__dict__)
print(Employee.__dict__)

#now we can change the raise amount for all
Employee.raise_amount=1.06
emp_1.raise_amount=2

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)




















