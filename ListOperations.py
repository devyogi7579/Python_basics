# There are two types of operations on List Data Structure

myList=[]
myList1=['July',7, '07.07.1972', '23.5','MSD', True, False, [7, 8, 9], [14, 15, 16]]

# 1. Fetching values from exisiting list, first 04 like string operations only
#==============================================================================
# type()       - to find the type of items
#---------------------------------------------------------#
print('Empty-Line'.center(50,'*'))
# print(myList1[2])                         # working
# print(myList1[5])                         # working
# print(myList1[8])                         # working
# print(type(myList1[2]))                   # working
# print(type(myList1[5]))                   # working
# print(type(myList1[8]))                   # working
print(f'the list item is "{myList1[1]}" and \n\tits type is "{type(myList1[1])}"')
print(f'the list item is "{myList1[2]}" and \n\tits type is "{type(myList1[2])}"')
print(f'the list item is "{myList1[5]}" and \n\tits type is "{type(myList1[5])}"')
print(f'the list item is "{myList1[8]}" and \n\tits type is "{type(myList1[8])}"')
print()
print('Empty-Line'.center(50,'='))

# len()        - to find the length of items
#---------------------------------------------------------#
# print(len(myList))                        # working
# print(len(myList1))                       # working
print(f"The length of '{myList}' is: '{len(myList)}'")
print(f"The length of '{myList1}' is: '{len(myList1)}'")
print()
print('Empty-Line'.center(50,'-'))

# -id()         - to find the memory allocation of items
#---------------------------------------------------------#
# print(id(myList))                         # working
# print(id(myList1))                        # working
print(f'The memory location for "{myList}" is: "{id(myList)}"')
print(f'The memory location for "{myList1}" is: "{id(myList1)}"')
print()
print('Empty-Line'.center(50,':'))

# slicing      - slicing with index numbers
#---------------------------------------------------------#
print(myList1[::])                      # prints entire list
print(myList1[2:5])                     # +ve printing Left to right
print(myList1[5:2:-1])                  # -ve printing right to left
print(myList1[-1])                      # prints last element of index
print(myList1[::-1])                    # Reverse printing
print()
print('Empty-Line'.center(50,'.'))

myList1=['July',7, '07.07.1972', '23.5','MSD', True, False, [7, 8, 9], [14, 15, 16]]
# index()      - to find the index of given items, available in the list
#---------------------------------------------------------#
# if the item is in with or without quotes then feed it in that way, inside index
print(myList1.index('July'))
print(myList1.index('MSD'))
print(myList1.index([7,8,9]))
print(myList1.index(True))          # without quotes,
print(myList1.index(7))             # without quotes
#print(myList.index(True,2,6))        # Index range not working in my case
print()
print('Empty-Line'.center(50,'~'))

# count()      - to find the count of items
#---------------------------------------------------------#
# you need to pass whole item together, you cannot say 07
print(myList1.count(True))                  # without quotes
print(myList1.count(7))                     # Not working
print(myList1.count('07.'))                 # Not working
print()
print('Empty-Line'.center(50,'~'))

#===========================================================================================================#
# 2. Modifying the list or list values
#===========================================================================================================#

myList2=['Apple', [15,16,17], 'Git', '2.50.1', 'pyhton3' ]

# append() Appending with new item at the end of list
#---------------------------------------------------------#
myList2.append('iphone')
myList2.append('mac-book')
# we cannot use: print(myList2.append('iphone')), 1st let append to happen then print the result
#myList2.append('iphone', 'Mac Book')    #Invalid---TypeError: list.append() takes exactly one argument (2 given)
# to append 5 items, we need to use append 5xtimes
print(myList2)
print('Empty-Line'.center(50,'<'))
print()
# to append an item at desired index, we need to use insert option

# insert() inserting an item at required index position
#---------------------------------------------------------#
myList2.insert(5,'ipod')    #insert(position,value) # insert sring
myList2.insert(2,'samsung')
myList2.insert(3,[10,12,14])    # insert List
print(myList2)
print('Empty-Line'.center(50,'>'))
print()

# extend()  Extending with new list
#---------------------------------------------------------#
# extend only works for list --- extend([a,b,c]), not with integers, float, strings
myList2.extend(['mac','linux','windows'])
print(myList2)
#---------------------------------------------------------#
# clear(), del(), copy(), remove() and pop()
# to clear the content of list
myList2.clear()
print(myList2)
print()

# del()
# to delete list or empty list, use
# del myList        # working
# print(myList)     #once you delete you get error like NameError: name 'myList' is not defined.
print(myList2)
#del myList2
#print(myList2)  #once you delete you get error like NameError: name 'myList2' is not defined.

# copy()
# to assign one list content to another list
myList3=myList2
myList2.append(45)      # we are performing operation on list 2
print(myList2)
print(myList3)          # the content of both lists are same, why because they have same id number
# But sometimes we just want content to get appended in one List say list2 and not in List3 then in that case
# Be clear it is very important, whenever we have to asssign 1 list value to another list then make sure to take copy
# bcoz of copy list2 and list3 will be completely different
print()
myList3=myList2.copy()
myList2.append(54)
print(myList2)          # list 2 will have its new appended content
print(myList3)          # and list 3 will not have appended content of list 2
print()

# remove()
# to remove list item
myList2=['Apple', [15,16,17], 'Git', '2.50.1', 'pyhton3' ]
myList2.remove('2.50.1')        # removes 2.50.1 from the list, 
# if you have two same values then removes remove only 1st value, in such case you have to use remove two times
print(myList2)
print()

# pop()
# to remove value from particular indexed position and then save it to another variable
myList2.pop()   # no index provided means default index is last value of the list
print(myList2)
myList2.append('Python3')
print(myList2[3])
RemovedPopValue=myList2.pop(2)      # you can capture removed pop value
print(myList2)
print(f'removed pop value is:', {RemovedPopValue})
print()

#---------------------------------------------------------#
# sort() sorts the list in assending order
# sort() and reverse() affects your original list, slicing doesnot
myNewList=[51,5.565,75.69,115,12]
mynewList=["car","bike","airplane", "Warplanes"]
myNewList.sort()            # Sort integers
mynewList.sort()            # Sort strings # Capital letters get priority over small letters
print(myNewList)        
print(mynewList)        
print()

# reverse()  sorts the list in descending or reverse order
myNewList.reverse()         # Sort integers in reverse order
mynewList.reverse()         # Sort strings # small letters get priority over Capital letters
print(myNewList)        
print(mynewList)        
print()

# spectial case:
myNewList=[51,5.565,75.69,115,12]
myNewList.sort(reverse=True)        # 1st sort then reverse
print(myNewList)

#### Imp: Replacing the existing value with a new value with the help of index values ####
# above operations are performed with the help of methods [append,insert, extend, deleting, sorting,reversing etc]

mynewList=["car","bike","airplane", "Warplanes"]
mynewList[1]='Bus'
mynewList[2]='ship'
mynewList[-1]='Warships'
print(mynewList)

#===========================================================================================================#