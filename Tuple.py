# tuple is used to store multiple values into a variable like lists
# Syntax: 
# myTuple=()            # empty tuple           
# myTuple = ()          # empty tuple   #both are correct with or without spaces
# to define single value, we need to give, but in list it is not required
# myTuple=('Apple',)    # Non empty tuple
# myTuple=('Apple')     # without , it is a normal data structure
myTuple=("hi",3,'3.5',[3.5,8], True)
#---------------------------------------------------------------------------------#
# properties of tuple data structure

# Useful to store any data structure, list, Boolean, integer, string, float
# The values in tuples are called items or elements
# All items/values/elements has to be seperated with (,) commas
# Tuples are ordered - tuple remember the order of items
# items in tuples are accessed by index
# len(myTuple) will give the number items
# if len of tuple is n, 
# then index values are from 0 to n-1 or -n to -1

####---- We cannot add/change/remove item(s) from tuple, this make tuple immutable, unaltering... 
# changes are not possible in tuple----####
# So tuple only have one kind of operations, which is FETCHING 
# dir(tuple) ---- only two operations are possible on tuple: count and index

# type (): find the type
#-------------------------------
myTuple=("hi",3,'3.5',[3,5,8], True)
print(myTuple)
print(type(myTuple))
print(f'The type of typle is: {type(myTuple)}')

myTuple=("hi")
print(myTuple)
print(type(myTuple))                # Single value without , # <class 'str'>

myTuple=(3)
print(myTuple)
print(type(myTuple))                # Single value without , # <class 'int'>

myTuple=("hi",)
print(myTuple)
print(type(myTuple))                # Single value with ,    # <class 'tuple'>

myTuple=(3,)
print(myTuple)
print(type(myTuple))                # Single value with ,    # <class 'tuple'>
print('End of line'.center(50,'-'))

# len(): find the length
myTuple=("hi",3,'3.5',[3,5,8], True)
print(f'The length of tuple is: {len(myTuple)}')
print('End of line'.center(50,'-'))

# id(): finding the memory location
myTuple=("hi",3,'3.5',[3,5,8], True)
print(f'The memory id of tuple is: {id(myTuple)}')
myTuple1=()
print(f'The memory id of empty tuple is: {id(myTuple1)}')
print('End of line'.center(50,'-'))

# slicing with index numbers [::]
myTuple=("hi",3,'3.5',[3,5,8], True)
print(myTuple[:])
print(myTuple[1:3:1])
print(myTuple[-1])
print(myTuple[::-1])                    #reverse printing
print('End of line'.center(50,'-'))

# index(): finding the index of a given value
myTuple=("hi",3,'3.5',[3,5,8], True)
print(f'The index of 3 in tuple is: {myTuple.index(3)}')
print(f'The index of list in tuple is: {myTuple.index([3,5,8])}')
print('End of line'.center(50,'-'))

# count(): finding the count of item from a given tuple, how many times that item is available inside tuple
myTuple=("hi",3,'3.5',[3,5,8], True, '3.5', 3)
print(f'The count of 3.5 in tuple is: {myTuple.count('3.5')}')
print('End of line'.center(50,'-'))
#---------------------------------------------------------------------------------#

