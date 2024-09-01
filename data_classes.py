# -*- coding: utf-8 -*-

#Data classes 

#lets create a simple class first and then compare it with dataclasses

class Investor:
    def __init__(self, name:str, age:int, cash:float,):
        self.name = name
        self.age = age
        self.cash = cash
     #its a represention of class, whenever you make an object of it, and print that object without parenthesis. this will show
    def __repr__(self):
        return f'Name: {self.name}'
    #if names of two objects are equal they are called equal
    def __eq__(self, other):
        return self.name == other.name
    #when cash of two objects are less than other one, it returns true
    def __lt__(self,other):
        return self.cash < other.cash
    
i1 = Investor('John', 22, 90000)
i2 = Investor('Ali', 34, 54333)
i3 = Investor('Bob', 66, 44333)

#repr will be called
print(i1)

#eq will be called, which returns false here
print(i1 == i2)

#here it returns True
i4 = Investor('John', 322, 44343)
print(i1 == i4)

#lt will be called
print(i1 < i3)

#now we use data classes to make things better
from dataclasses import dataclass

#so the dataclass makes the repr,lt,eq methods automatically and we dont even need to create the init consctructor
@dataclass
class Investor:
    name: str
    age: int
    cash: float
    
i1 = Investor('John', 22, 90000)
i2 = Investor('Ali', 34, 54333)
i3 = Investor('Bob', 66, 44333)

#it gives dataclass repr
print(i1)

#the following return false
print(i1 == i2)

#this return True
i4 = Investor('John', 22, 90000)
print(i1 == i4)


#we can also add new fields for the above class and everything will be taken care off by data class

@dataclass
class Investor:
    name: str
    age: int
    cash: float
    color: str
    
i1 = Investor('John', 22, 90000,'blue')
i2 = Investor('Ali', 34, 54333,'green')
i3 = Investor('Bob', 66, 44333,'yello')

#it gives dataclass repr
print(i1)

#the following return false
print(i1 == i2)

#this return True
i4 = Investor('John', 22, 90000,'blue')
print(i1 == i4)

#now if we dont want the dataclasses prebuilt methods we can always override them as below

@dataclass
class Investor:
    name: str
    age: int
    cash: float
    color: str
    
    def __repr__(self):
        return 'hello'
    
i1 = Investor('John', 22, 90000,'blue')
i2 = Investor('Ali', 34, 54333,'green')
i3 = Investor('Bob', 66, 44333,'yello')

#now the repr is overriden but he rest is as before
print(i1)

#there is a better attribute of dataclass by which we can ignore or set default for certain fields
from dataclasses import dataclass, field

@dataclass
class Investor:
    name: str
    #we can set default value to a field too
    age: int = field(default=0)
    #we want the cash to be ignored in repr and comparisons, default fields should always come last
    cash: float = field(repr= False, compare= False, default=0.0)
    
i1 = Investor('John', 22, 90000)
i2 = Investor('Ali', 34, 54333)
i3 = Investor('Bob', 66, 44333)

#now it outputs only the first two fields .e.g: Investor(name='John', age=22)
print(i1)

#now the following is true
i4 = Investor('John', 22, 80)
print(i1 == i4)

#here we use the default age
i5 = Investor('John')
print(i5)
#the following command gives error so we can solve it after
print(i1 > i4)

#making comparisons work in the default way
@dataclass(order=True)
class Investor:
    name: str
    #we can set default value to a field too
    age: int 
    #we want the cash to be ignored in repr and comparisons, default fields should always come last
    cash: float 
    
i1 = Investor('John', 22, 90000)
i2 = Investor('Ali', 34, 54333)
i3 = Investor('Bob', 66, 44333)

#the following command gives error so we can solve it after
print(i1 > i3)


#making comparisons work in the overriden way
@dataclass(order=True)
class Investor:
    #we put a sort index which we dont initilaize at first and we dont want to be represented
    sort_index: float = field(init=False, repr=False)
    name: str
    #we can set default value to a field too
    age: int 
    #we want the cash to be ignored in repr and comparisons, default fields should always come last
    cash: float 
    
    #now we gonna set the sort_index after the init is done or fields has a value
    def __post_init__(self):
        #we want to sort based on the cash size
        self.sort_index = self.cash
    
i1 = Investor('John', 22, 90000)
i2 = Investor('Ali', 34, 54333)
i3 = Investor('Bob', 66, 44333)

#the following command gives error so we can solve it after
print(i1 > i3)

#we can also sort the above all at once

mylist = [i1, i2, i3]
mylist.sort()
print(mylist)
print(hash(i1))

#we can also hash our class
@dataclass(order=True, unsafe_hash=True)
class Investor:
    #we put a sort index which we dont initilaize at first and we dont want to be represented
    sort_index: float = field(init=False, repr=False)
    name: str
    #we can set default value to a field too
    age: int 
    #we want the cash to be ignored in repr and comparisons, default fields should always come last
    cash: float 
    
    #now we gonna set the sort_index after the init is done or fields has a value
    def __post_init__(self):
        #we want to sort based on the cash size
        self.sort_index = self.cash
    
i1 = Investor('John', 22, 90000)
i2 = Investor('Ali', 34, 54333)

print(hash(i1))
print(hash(i2))


