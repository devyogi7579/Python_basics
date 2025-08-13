#Type conversion means converting 1 data type into another
# list to tuple--- use with tuple()
# tuple to list --- use with list()
# string to list or tuple --- with split()
# Number/Boolean/None data to list or tuple ---with[] and ()
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

myList=[13, 3.14, 'star', [15, 16.353, 21.9], True]
myTuple=('oracle','mongoDB','mySql','Python','vscode')

# convert list into tuple ---with tuple()
print(tuple([13, 3.14, 'star', [15, 16.353, 21.9], True]))
print(tuple(myList))
myNewTuple=(tuple(myList))
print(myNewTuple)
print()

# convert tuple into list ----with list()
myNewList=(list(myTuple))
print(myNewList)
print()

# convert string into list  --- with split()
myStr='I am enjoyig learning python'
# split based on spaces
print(myStr.split())                        # the default conversion of string is into list
Mynewlist=(myStr.split(sep=' '))
print(Mynewlist, type(Mynewlist))   
print()
myStr='I am \nenjoyig learning \npython'
Mynewlist=(myStr.split(sep='\n'))
print(Mynewlist, type(Mynewlist))
print()

# convert string into tuple
myStr='I am enjoyig learning python'
# split based on spaces
Mynewlist=(tuple(myStr.split(sep=' ')))
print(Mynewlist, type(Mynewlist))

# string into single list or tuple
myStr='I am enjoyig learning python'
myNum=(56)
myNewList=[myStr,myNum]
print(myNewList, type(myNewList))
print()
myNewTuple=(myStr)                      # Dont forget to add ,
print(myNewTuple, type(myNewTuple))
print()
myNewTuple=(myStr,myNum)                 
print(myNewTuple, type(myNewTuple))
