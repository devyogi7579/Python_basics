# Nested if else Conditional statements
# Read any number between 1 to 10 and display the given numbers is even or odd

ReadNum=int(input('Enter number of your choice: '))
print(type(ReadNum))
result=ReadNum%2
print(result)

if result == 0 :
    print(f'Number entered {ReadNum} is even')

if result == 1:
    print(f'Number entered {ReadNum} is odd')
#-----------------------------------------------------------------------------
# the ReadNum%2, cannot be 0 or 1, at a same time, so we will put it inside, one block of if condition
print()
if result == 0 :
    print(f'Number entered {ReadNum} is even')
else:
    print(f'Number entered {ReadNum} is odd')
#-----------------------------------------------------------------------------
print()
if result == 1 :
    print(f'Number entered {ReadNum} is odd')
else:
    print(f'Number entered {ReadNum} is even')
#-----------------------------------------------------------------------------
print()
if result :             
# No condition means, 0 which means false, 6%2=0 but 0 means false here, so change output accordingly
    print(f'Number entered {ReadNum} is odd')
else:
    print(f'Number entered {ReadNum} is even')

#-----------------------------------------------------------------------------
print()
if ReadNum%2 :             # Keeping expression directly
    print(f'Number entered {ReadNum} is odd')
else:
    print(f'Number entered {ReadNum} is even')
#==================================================================================
# To validate, if number entered is in the given range say [1 to10]
print()
ReadNum=int(input('Enter number of your choice: '))

#numRange=[1,2,3,4,5,6,7,8,9,10]     
# so if number range is 1 to 100 then    
numRange=range(0,100,1)
# print(numRange)
# we will validate here, if entred num is in num range or not
if ReadNum in numRange :
    print(type(ReadNum))
    result=ReadNum%2
    if ReadNum%2 :                                     
        print(f'Number entered {ReadNum} is odd')
    else:
        print(f'Number entered {ReadNum} is even')
else:
    print('Entred number is out of 1 to 100 range')

# The above block of code is called NESTED if else block of code....
