#how to read property file
#property file extention is .properties
#it is a flat file (text file) used to store data as key-value pair
from pyjavaproperties import Properties

p=Properties() #create object
p.load(open('../config.properties')) #open the file
v=p['BROWSER'] #get the value
print(v)
v=p.getProperty('ITO')
print(v)