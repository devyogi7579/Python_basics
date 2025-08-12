#List is a data structure to store multiple values into a variable
# syntax:   myList=['items'] (without_spaces), 
#           myList = ['items'] (with_spaces), both is correct, no problem
# List means square brackets [] and they are MUTABLE...

myList=['July', '07', '07.07.1972', '23.5','MSD', True, False, [7, 8, 9], [14, 15, 16]]

#properties of list data structure
#---------------------------------------------
# 1. List can have, any number of values, of any type(another data structure too), 
# 2. Values inside list are called items or elements
# 3. all items need to be (,) seperated 
#   integers,               #Need to be quoted
#   floats,                 #Need to be quoted
#   strings,                #Need to be quoted
#   Booleans or             #Not to be quoted
#   lists itself in it      #Not to be quoted, must be , seperated
# 4. List remembers the order of items inserted (maintains the sequence in which data entered)
myList=['July', '07', '07.07.1972', '23.5','MSD', True, False, [7, 8, 9], [14, 15, 16]]
print(myList)
print()

# 5. List items are accessed by index, index starts with 0 and you can accessed required value from list
print(myList[3])            # prints 3rd element of the list
print(len(myList))          # prints length of list, len will give number of item in list
print()

# if length of the list is n then index values are from 0 to n-1 or -n to -1
print(myList[(len(myList)-1)])  # prints last element of the list
print()

# we can "add/change/remove" item(s) from a list at any time.
# Thats why list are called "mutable data structure"...
#Remember: "strings are immutable" but "list are mutable"
myList.remove('July')
print(myList)   #July will be removed