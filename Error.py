# Error (mistakes)
# Types of errors
    # 1. Syntax Errors:
#--------------------------------------------------------------------------------
#   File "/home/av7579/python/Demo.py", line 3
#     print("I am happy to see my output is print on the terminal"
#          ^
# SyntaxError: '(' was never closed
#--------------------------------------------------------------------------------
# Python tells about line number where error is and type of error
# Occurs if we do not follow the correct syntax
# Script executes only if all syntax errors are corrected
# There is no way to handle Syntax Errors

#=================================================================================#
    # 2. Logic Errors aka Logical Error or Runtime Error or Exceptions
# Expcetions: Some errors only occurs in some situation only
#             Occurs only if any Logical Errors - But not always
#               Syntax wise expression is correct but logic wise it is not
#             There is a way to handle exception errors
#--------------------------------------------------------------------------------
# Traceback (most recent call last):
#   File "/home/av7579/python/Condition_ifelifelse.py", line 73, in <module>
#     NumDict!={
#     ^^^^^^^
# NameError: name 'NumDict' is not defined
#--------------------------------------------------------------------------------

#=================================================================================#
# Types of exceptions:
#-------------------------------------
# Errors occurs during runtimes  are called exceptions
# we have different types of exceptions
# x=5
# print(x,y)            # NameError
# x='hi'
# y=int(x)              # ValueError     
# 4/0                   # ZeroDivisionError:
# 'hi'.upper()          # IndentationError:
# "hi".reverse()          # # AttributeError:

# To list all types of errors
#-------------------------------------
# dir(locals()['__builtins__'])

# We can also define our custom exceptions