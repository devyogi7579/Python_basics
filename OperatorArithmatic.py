# Different types of Arithmatic operations are

# Addition (+)                  # Valid for Numbers, strings, List, Tuple, (NA for Dictionaries)
# Subtraction (-)               # Valid for Numbers, (NA for Dictionaries)
# Multiplication (*)            # Valid for Numbers, strings, List, Tuple, (NA for Dictionaries)
# Division (/)                  # Valid for Numbers, (NA for Dictionaries)
# Modulus (%)                   # Valid for Numbers, (NA for Dictionaries)
# Floor Division (//)           # Valid for Numbers, (NA for Dictionaries)
# Exponential (**)              # Valid for Numbers, (NA for Dictionaries)
#=========================================================================================================#

# Addition (+)
#--------------------------------
# sum of two numbers
print(3+5)                  # Addition of integers
print(float(3.5+5.65))      # Addition of float
print('Ap'+"ple")           # Addition of strings without space
print("3"+"5")              # Addition of strings 
print('Ap'+' '+"ple")           # Addition of strings with space
print([5,5,5]+[3,3,3]+['a','b','c'])      # Addition of list
print((5,5,5)+(3,3,3)+("a","b","c"))      # Addition of tuple

# Instead of directly displaying, if we want to store it into variable that is possible
# a=input('Enter first number: ')
# b=input('Enter second number: ')
# sumOfab=(a+b)
# print(f'The sum of {a} and {b} is: {sumOfab}')
# print()
# # You will get response as string, to convert it into integer change the type
# a=int(input('Enter first number: '))
# b=int(input('Enter second number: '))
# sumOfab=(a+b)
# print(f'The sum of {a} and {b} is: {sumOfab}')          #{} = placeholder
# print()
# print(f'The sum of {a} and {b} is: {a+b}')  
print()

# subtraction (-)
#--------------------------------
print(13-3)
print(f'The "subtraction" of {13} and {3} is: {13-3}')
print(1-13)
print(f'The "subtraction" of {3} and {13} is: {3-13}')
print(float(3.5-5.65))
print()

# Multiplication (*) 
#--------------------------------
print(f'The "multiplication" of {3} and {13} is: {13*3}')
print(float(3.5*5.65))
print('python'*3)       # pythonpythonpython                    # store this in variable, if needed
print(('python')*3)     # pythonpythonpython                    # Without ,
# tuple multiplication
print(('python',)*3)    # ('python', 'python', 'python')        # With ,
# List multiplication
print(['python',]*3)    # ['python', 'python', 'python']        # with ,
print()

# Modulus (%) 
#--------------------------------
print(13%3)
print(f'The "modulus" of {13} and {3} is: {13 % 3}')
print(float(3.5/5.65))
print()

# Floor Division (//): it will do division and then down it to the nearest whole number
#--------------------------------
print(13//3)
print(f'The "Floor Division" of {13} and {3} is: {13 // 3}')        #13//3 = 4.33 = down to nearest integer 4
print(float(9.25//3.5))
print()

# Exponential (**): 
#--------------------------------
print(3**3)
print(f'The "Exponential" of {3} and {3} is: {3 ** 3}')        #13//3 = 4.33 = down to nearest integer 4
print(float(3.5**3.5))
print()

# List + tuple: Not possible
#--------------------------------
#print((3,4)+[3,4])              #TypeError: can only concatenate tuple (not "list") to tuple
print((3,4)+(3,4))
print([5,6]+[5,6])
print((3,4)*5)      # *3.5 not possible
print([5,6]*5)