# -*- coding: utf-8 -*-

class Employee:
  
    def __init__(self,first,last,pay):
        self.first=first #possible option: self.fname=first
        self.last=last #optional: self.lname=last
        self.pay=pay
        self.email=first + '.' + last + '@company.com'
      
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
   
#now we can create instances
emp_1=Employee('Corey','Schafer',50000)
emp_2=Employee('Test','User',60000)

#we get the object of emp_1
print(emp_1)

#compare the above print(emp_1) with the following



class Employee:
   
    def __init__(self,first,last,pay):
        self.first=first #possible option: self.fname=first
        self.last=last #optional: self.lname=last
        self.pay=pay
        self.email=first + '.' + last + '@company.com'
       
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
 
    
    def __repr__(self):
        
        return "Employee('{}','{}','{}')".format(self.first, self.last,self.pay)

    def __str__(self):
        
        return '{}-{}'.format(self.fullname(), self.email)
    
    def __add__(self,other):
        return self.pay + other.pay
#now we can create instances
emp_1=Employee('Corey','Schafer',50000)
emp_2=Employee('Test','User',60000)

#here we get a description of emp1
print(emp_1)
print(repr(emp_1))
print(str(emp_1))
#the above prints are same as the following

print(emp_1.__repr__())
print(emp_1.__str__())

#to addd to employees we can use this type of dunder method

print(emp_1 + emp_2)

#the following two are same

print(len('test'))
print('test'.__len__())







