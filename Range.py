# range(): it returns sequence of integer numbers
# starting from 0 and with step as 1, by default,
# and stops before specified number
# syntax:      range(start,stop,step)      # by  default step is +1    # this returns sequence of integer numbers
# this logic same as string slicing concepts
# ================================================================#

# to print 0 to 6 numbers
print(range(0,6,1))         
# Step is +ve, 
# direction is left to right
# You will going to get some value
# #0+1=1,1+1=2,2+1=3 and so on
print(range(0,6))           # by default step is 1
# output = range(0, 6), which is an OBJECT, which we will see later
# usint for loop we can get those values
# else convert OBEJCT o/p into LIST or tuple type, both is possible
print(list(range(0,6)))
print(tuple(range(0,6)))
print()
#------------------------------------------------------------------------#
# -ve range
print(list(range(0,-5,-1)))         # output is possible 0+-1=-1-1=-2-1=-3=-3-1=-4 and so on
print(list(range(0,-5)))            # output is not possible, bydefault step = +1,
print()
# step and range directions are opposite, output = emptyList
#------------------------------------------------------------------------#
print(range(8))         # single value means its an end value
print(list(range(8)))
print()

####IMPORTANT POINT#### To get indexed values from string, list or tuple
#-----------------------#

myStr="Python"
print(len(myStr))
# From this length we can generate range, how
print(list(range(len(myStr))))          # list -- range -- len -- variable

myList=['Hi', 'Helllo', 'how', 'are', 'you']
print(list(range(len(myList))))
print()

myTuple=('Hey','buddy','I ', 'am', 'fine')
print(list(range(len(myTuple))))
print()
###=========================================================================###

print(list(range(0,11,2)))        # prints even number
print(list(range(1,10,2)))        # prints even number
