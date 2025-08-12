# Dictionary is one of the data structure and is used to store multiple key-value pairs
# Syntax: myDict = {}        # with spaces valid
# myDict={"strkey":value, "strkey":value, numKey="strValue"}
# myDict={"a":7, "b":9, "c":7, 9:"nine"}        # without spaces valid

#properties of dictionary data structure
# 1. Useful to store any number of key-value pairs
# 2. Key always from 
#               Numbers/strings/Boolean/none data type {List and tuple not allowed}
#   But the  value could be any data {list, tuple, dictionary, num, string, boolean, none}
# 3. if string is used either in key or value place, then use "quotes"
# 4. All key value pair has to be "seperated by commas(,)" 
# 5. Duplicate "Keys are not allowed" but "values are allowed"
# 6. key-value pairs are called "items"
# 7. len(myDict)returns number of key-value pairs
#---------------------------------------------------------------------------------------
# 8. Indexing and slicing concepts are "not allowed" for dictionaries
#---------------------------------------------------------------------------------------
# 9.Dictionary key-value "paired are ordered"
# ======================================================================== #
# Operations on Dictionary Data structure
# 1. Fetching values from Dictionary
#---------------------------------------------------------------------------------------
# -type()   -len()    -id()    -keys()     -values()    -items()
# finding the value of a given key -[key] or get(key) -> get() method is the best choice

# student = {                                   # Keys are uniqe
#     "id": 101,                                # value is num, unquoted
#     "name": "Alice",                          # value is str, quoted
#     "age": 22,        
#     "course": "Computer Science",
#     "grades": {"math": 90, "physics": 85},    # value is dictionary
#     "active": True                            # value is Boolean, unquoted
# }

#or 
student = {"id": 101,"name": "Alice","age": 22, "course": "Computer Science","grades": {"math": 90, "physics": 85},"active": True}
# Both representation is correct

# To print
print(student, type(student), len(student), id(student))
print()

# To print, only Keys from your dictionary
stuKey=student.keys()
print(stuKey, type(stuKey))         #<class 'dict_keys'>
print()
# to convert 'dict_keys' into list then use
print(list(stuKey),type(stuKey))
print()

# To print, only values from your dictionary
stuValues=student.values()
print(stuValues, type(stuValues))   #<class 'dict_values'>
print()
# to convert 'dict_values' into list then use
print(list(stuValues),type(stuValues))
print()

# To access any value from dictionary we dont have any concept of index values
# but with Keys we can get those values
# Note: if keys are quoted/unquoted, then provide as it is...
print(student['name'])
print(student['id'])
print(student['grades'])
# To extract keys inside another dictionary
print(student['grades']['math'])
# if key is not present, then we get keyError
#print(student['email'])     
# instead of this we can get some default values, for this use get() method
print(student.get('Email',"No value found"))
print(student.get('name',"No value found"))
print(student.get('age',"No value found"))
print(student.get('course',"No value found"))
# using get we can pass default message to value, 
# get() method is better than printing key values like print(student['name'])
print(student.get('Email')) # if no value message provided then it will print 'None'
# ======================================================================== #
# 1. Modifying values from Dictionary 
#---------------------------------------------------------------------------------------
# Create a dictionary:
#               myDict={"Hi":"Hello"}
#               myDict=dict.fromkeys((k1,k2),value)     # To pass same values to all keys we have 'fromkeys'
myDict=dict.fromkeys(("tim24", "jim26", "kim45", 101), 'developer') # keys are passed as tuple
print(myDict)
print()
# we can also store our keys into some variables
#----------------------------------------------------
myKeys=('ap32','rl245','be142', 119)
print(myKeys, type(myKeys))
mynewDict=dict.fromkeys(myKeys,'tester')
print(mynewDict, type(mynewDict))

# add or update key value pairs
#----------------------------------------------------
#               mynewDict[key]=value     # if you have key already exisiting then it will update that value
mynewDict['tl81']='test controller'
print(mynewDict)
print()
# Another syntax
#----------------------------------------------------
#               mynewDict.update({key:value})  # we provide KV pair as a dictionary
mynewDict.update({'kr35':'test auditer'})
print(mynewDict)
print()

# add only if key is not existing
#----------------------------------------------------
# syntax:   mynewDict.setdefault(key,value)     # update only if keyis not existing and also return the values
# This will return KV pair, as it is, will not append, bcoz KV pair already exists
print(mynewDict.setdefault('kr35','test auditer'))
# or
myDicadd=mynewDict.setdefault('kr35','test auditer')        # storing value in some variable
print(f'Output from setdefault cmd: {myDicadd}')            # prints the value added
print()

# This will add the KV pair
print(mynewDict.setdefault('glk1','test adm'))              # prints the value added
print()

# to remove or delete a key-value pair
#----------------------------------------------------
    # Syntax: mynewDict.pop(key) 
myDictremove=mynewDict.pop('kr35')                          # We pass key to removed, we can capture value removed
print(f'Item removed from dictionary: {myDictremove}')      # but prints the value removed
print(myDictremove)

print(f'The value removed from dictionary: {mynewDict.pop('be142')}')
# after deletion, to check updated dictionary
print(mynewDict)
print()

# to remove or delete last inserted KV pair
#----------------------------------------------------
mynewDict.update({'gk19':'admin'})
print(mynewDict)
# syntax: mynewDict.popitem()
#myDictrem=mynewDict.popitem('gk19') # popitem() takes no arguments, bcoz popitem job is to remove newly added item
deltedItem=mynewDict.popitem()           
print(deltedItem)                    # reture delete item (both Key and values) --- ('gk19', 'admin')
print(mynewDict)

# to remove or delete all inserted KV pair, means making dict = empty
#----------------------------------------------------------------------
# Syntax:
#            mynewDict.clear()
mynewDict.clear()
print(mynewDict)            # this will show empty directory
# to remove dictionary
del mynewDict
#print(mynewDict)            # throws error bcoz nothing to print

# to copy a dictionary to another dict without same refrence
#----------------------------------------------------------------------
# Syntax:
#            mynewDict=myDict.copy()    

# Without copy both will have same id, means changes made in 1 dictionary will be reflected in another dictionary
mynewDict=myDict
print(f'id of myDict = {id(myDict)} \nid of my new Dict = {id(mynewDict)}')
# both are same

mynewDict=myDict.copy()
print(f'new dictionary copied from exisitng dict is: \n{myDict}')
print(f'{id(myDict)}, \n{id(mynewDict)}')
print()

# be careful whenever you're assigning 1 list or dictionary value to another list or dictionary

# ======================================================================== #