# -*- coding: utf-8 -*-

class Employee:
   
    def __init__(self,first,last):
        self.first=first #possible option: self.fname=first
        self.last=last #optional: self.lname=last
        self.email=first + '.' + last + '@company.com'
       
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
   
emp_1=Employee('Corey','Schafer')

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname())

#lets now change our name and print to see what is the difference
emp_1.first='Jim'


print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname())

#in the above prints as you can see the email has not changed so for this we need to do the following



class Employee:
    def __init__(self,first,last):
        self.first=first #possible option: self.fname=first
        self.last=last #optional: self.lname=last
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first,self.last)
    #@property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
   
emp_1=Employee('Corey','Schafer')

emp_1.first='Jim'
print(emp_1.first)
#we do not put the @property decorator above the email method in our class we have to do the following
#print(emp_1.email())
#if we put the @property decorator above our method we can call the method as an attribute
print(emp_1.email)
print(emp_1.fullname())

#in the above code we could change the first name but we can not fullname like that, for which we need setter
emp_1.fullname='Corey Schafer' #this will give error but the following is the solution




class Employee:
    def __init__(self,first,last):
        self.first=first #possible option: self.fname=first
        self.last=last #optional: self.lname=last
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first,self.last)
    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    #setter name has to be same as method name
    @fullname.setter
    def fullname(self,name):
        first, last= name.split(' ')
        self.first=first
        self.last= last
        
    #we can create deleters
    @fullname.deleter
    def fullname(self):
        print('Delete Name:')
        self.first=None
        self.last= None
        
        
    
    
    
    
emp_1=Employee('Corey','Schafer')

emp_1.fullname='Joji Kaffer'


print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)


del emp_1.fullname














