# -*- coding: utf-8 -*-

#option one
#a class is a blueprint for creating instances
class Employee:
    pass

#now we can create instances
emp_1=Employee()
emp_2=Employee()
print(emp_1)
print(emp_2)

emp_1.first='Corey'
emp_1.last='Schafer'
emp_1.email='Corey.Schafer@company.com'
emp_1.pay=50000

emp_2.first='Test'
emp_2.last='User'
emp_2.email='Test.User@company.com'
emp_2.pay=60000


print(emp_1.email)
print(emp_2.email)



#option two
#now we can wrap the above code inside class too like the following
#self is the instance
class Employee:
    def __init__(self,first,last,pay):
        self.first=first #possible option: self.fname=first
        self.last=last #optional: self.lname=last
        self.pay=pay
        self.email=first + '.' + last + '@company.com'



#now we can create instances
emp_1=Employee('Corey','Schafer',50000)
emp_2=Employee('Test','User',60000)
print(emp_1.email)
print(emp_2.email)

#lets create an actions, we can do it this
print('{} {}'.format(emp_1.first,emp_1.last))

#option Three

#we can do the above action better, by creating method inside the class as follow
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
print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())

#we can do the following too, so we need to manually pass the instance emp_1
print(Employee.fullname(emp_1))


#note: the following code without self, gives an error
#error: fullname() takes 0 positional arguments but 1 was given


class Employee:
    def __init__(self,first,last,pay):
        self.first=first #possible option: self.fname=first
        self.last=last #optional: self.lname=last
        self.pay=pay
        self.email=first + '.' + last + '@company.com'

    def fullname():
        return '{} {}'.format(self.first,self.last)

#now we can create instances
emp_1=Employee('Corey','Schafer',50000)
emp_2=Employee('Test','User',60000)

print(emp_1.fullname())

#Reason:when we call emp_1.fullname(), the emp_1 get passed as an instance but fullname does not have one

