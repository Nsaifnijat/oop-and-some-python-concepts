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
        self.pay=int(self.pay * self.raise_amount)


#EXAMPLE 1
class Developer(Employee):
    pass

#now we can create instances
dev_l=Developer('Corey','Schafer',50000)
dev_2=Developer('Test','User',60000)

print(dev_l.email)
print(dev_2.email)

#to show the inherited things along the stages of inheritance
print(help(Developer))


#EXAMPLE 2
#now we want our developers to has a higher raise amount
class Developer(Employee):
    raise_amount=3

#now we can create instances
dev_1=Developer('Corey','Schafer',50000)
emp_1=Employee('Test','User',60000)

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)


#EXAMPLE 3

class Developer(Employee):
    raise_amount=3
    def __init__(self, first, last, pay,prog_lan):
        super().__init__(first, last, pay)
        self.prog_lan = prog_lan
        
dev_1=Developer('Corey','Schafer',50000,'python')

print(dev_1.email)
print(dev_1.prog_lan)
        

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees=[]
        else:
            self.employees=employees
            
    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def print_emps(self):
        for emp in self.employees:
            print('--->', emp.fullname())
            
        
dev_l=Developer('Corey','Schafer',50000,'Python')
dev_2=Developer('Test','User',60000,'Java')

mgr_1=Manager('sue', 'smit', 90000,[dev_1])
print(mgr_1.email)

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)

mgr_1.print_emps()         


#to check mgr_1 instace of which class is it
print(isinstance(mgr_1,Employee))
print(isinstance(mgr_1,Manager))
#issubclass also used
print(issubclass(mgr_1,Manager))























