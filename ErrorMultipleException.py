# Multiple Exception Handling
#-----------------------------------------

# syntax
# Detailed exception handling for better readablity [recomended one]
'''
try:
except Exception1
except Exception2
except Exception3
except Exception as e:  [Code for unknown exception]
'''
# Combining (Compact) exception handling
'''
try:
except (Exception1, Exception2, Exception3)         # All exceptions are in 1 line
except Exception as e:  [Code for unknown exception]
'''
#===================================================================================#

a=int(input('Enter 1st number: '))
b=int(input('Enter 2nd number: '))

div_ab=a/b

print(f'The Division of {a} with {b} is: {div_ab}')

# Now we can see two exception handling possibilities here
# 1) Non integer number entred by user
# 2) Division by zero
print(1)
# try:
#     a=int(input('Enter 1st number: '))      #invalid literal for int() with base 10: '5rt'
#     b=int(input('Enter 2nd number: '))      # division by zero
#     div_ab=a/b
#     print(f'The Division of {a} with {b} is: {div_ab}')
# except Exception as e:
#     print(f'The exception is because of: {e}')
#     print('Non integer number entred by user')
#--------------------------------------------------------#
# Detailed exception handling [Recomended one]
print(2)
try:
    a=int(input('Enter 1st number: '))
    b=int(input('Enter 2nd number: '))
    div_ab=a/b
    print(f"The Division of '{a}' with '{b}' is: '{div_ab}'")
except ValueError:
    print('Your input must be an Integer')
except ZeroDivisionError:
    print('Your 2nd input must be non-zero')
except Exception as e:
    print(f'The exception is because of: {e}')

#--------------------------------------------------------#
# Combining (Compact) exception handling
print(3)
try:
    a=int(input('Enter 1st number: '))
    b=int(input('Enter 2nd number: '))
    div_ab=a/b
    print(f"The Division of '{a}' with '{b}' is: '{div_ab}'")
except (ValueError, ZeroDivisionError):
    print('Your input must be an Integer and 2nd input must be non-zero')
except Exception as e:
    print(f'The exception is because of: {e}')
    