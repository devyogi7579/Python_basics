#Exception Handling:
    # It is a way to handle runtime errors
    # We have try and except statements to handle Python Exceptions/Runtime errors
# Syntax
'''
----------------------------------
try:
except Exception as e
else:
finally:
----------------------------------
'''

#try:                        # Code that may cause an exception
#except Exception as e :     # Code to handle exception, in place of e we can pass any name or character
#else:                       # Code to handle if no exception raised (we can keep this in try block also)
#finally:                    # Code that will always be executed, regardless of exceptions

print(1)
readnum=int(input('Enter number: '))
print(f'The number entered by user is: {readnum}')
print()
# ValueError: invalid literal for int() with base 10: '25rt'
#---------------------------------------------------------------------------------------#
try: 
    readNum=int(input('Enter number: '))    # if user passes 5trt
    # if there is a problem in try block then code enters into except block
except Exception as e:
    print('Please provide integers only')
#---------------------------------------------------------------------------------------#
# print(f'The number entered by user is: {readNum}')  # with this print we get an error like NameError: name 'readNum' 
# fot this print also we can provide exception like
try:
    print(f'The number entered by user is: {readNum}')
    exit()
except Exception  as  e:
    print('Non integer value provided by user')

print()
#---------------------------------------------------------------------------------------#
# Another way is, we can put print in try block only
print(2)
try: 
    readNum=int(input('Enter number: '))    # if user passes 5trt
    print(f'The number entered by user is: {readNum}')
    exit()
except Exception as e:
    print('Please provide integers only')

print()
#---------------------------------------------------------------------------------------#
# We can also print the error captured by "e"
print(3)
try: 
    readNum=int(input('Enter number: '))    # if user passes 5trt
    print(f'The number entered by user is: {readNum}')
    exit()
except Exception as e:
    print(e)                # invalid literal for int() with base 10: '6ytt'
    print('Please provide integers only')

print()
#---------------------------------------------------------------------------------------#
# If you know  what kind of exception occurs, use "except ValueError :"
print(4)
try: 
    readNum=int(input('Enter number: '))    # if user passes 5trt
except ValueError :                         # if you know what kind of exception error occurs
#except Exception as e:                     # else go with this
    print('Please provide integers only')

print()
#=========================================================================================#
# try -except -else
print(5)
try:
    readNum=int(input('Enter number: '))    # Which will consist of some errors
except Exception  as  e:
    print('Non integer value provided by user')
else:
    print(f'The number entered by user is: {readNum}') 
print()

#=========================================================================================#
# try -except -else -finally
print(6)
try:
    readNum=int(input('Enter number: '))    # Which will consist of some errors
except Exception  as  e:
    print('Non integer value provided by user')
else:
    print(f'The number entered by user is: {readNum}') 
finally:
    print(f'It always executes irrespective of errors and exceptions')
print()
#=========================================================================================#
# try -except -else
print(7)
try:
    readNum=int(input('Enter any number between 1 to 5: '))
    EnteredNum=range(1,6,1)
    if readNum == 1:
        print(f"Entered number '{readNum}' in word is : one")
    elif readNum == 2:
        print(f"Entered number '{readNum}' in word is : two")
    elif readNum == 3:
        print(f"Entered number '{readNum}' in word is : three")
    elif readNum == 4:
        print(f"Entered number '{readNum}' in word is : four")
    elif readNum == 5:
        print(f"Entered number '{readNum}' in word is : five")
    else:
        print('Entered Num is not in our range')
    print()
except Exception as e:
    print(e)
    print('Non integer value provided by user')
else:       # This is optional piece of code
    print(f'The number entered by user is: {readNum}') 