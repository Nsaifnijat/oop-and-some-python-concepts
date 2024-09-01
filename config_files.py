# -*- coding: utf-8 -*-

#here we can import the content of our config file
from configparser import ConfigParser


#reading config file
file='config.ini'

config = ConfigParser()
config.read(file)

#getting sections of our config file
print(config.sections())

print(config['account'])
#we can also return it as a list
print(list(config['account']))

#access elements

print(config['account']['pin'])
print(config['account']['status'])

#updating our sections

config.add_section('Address')
config.set('Address','name','Barchi')

#now we need to write the above in our config file

with open(file, 'w') as configfile:
    config.write(configfile)










