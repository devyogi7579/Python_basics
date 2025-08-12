# Learning case conversion #            # 07th August 2025
# Note:In any case conversion your original value doesnt change

# to lower case
myStr='Take Any String'
print('original string:',myStr)
print('Result:',myStr.lower())
print()

# to upper case
myStr='Take Any String'
print('original string:',myStr)
print('Result:', myStr.upper())
print()

# to title case
myStr='title case test'
print("Original string:",myStr)
print('Result:',myStr.title())
print()

# to capitalize
myStr='title case test'
print("Original string:",myStr)
print('Result:',myStr.capitalize())
print()

# to swapcase
myStr='Take Any String'
print('original string:',myStr)
print('Result:', myStr.swapcase())
print()

#Note: Strings are immutable: meaning: once string is defined then it can be changed 
# but we can re-declare it with new value

myStr='limca'   #this immutable
myNewStr=(myStr.upper())
print('original string:', myStr)
print('re-declared string:', myNewStr)
print()
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
# Case Validation: If we want to validate if my string is in upper,lower or titlecase or something like that
# during such case we will use these operation or method
# Result  of case validation is only TRUE or FALSE (means Boolean DATA)
# Example of case validation operation are
myStri='Limca360'
myStrn='360'
print(f'Is my string "{myStr}" is lowercase:', myStr.islower())
print(f'Is my string "{myStr}" is uppercase:', myStr.isupper())
print(f'Is my string "{myStr}" is titlecase:', myStr.istitle())
print(f'Is my string "{myStr}" is alphabetic string:', myStr.isalpha())
print(f'Is my string "{myStri}" is alphabetic string:', myStri.isalpha())
print(f'Is my string "{myStri}" is alphabetic string:', myStri.isalnum())
print(f'Is my string "{myStri}" is digit string:', myStr.isdigit())
print(f'Is my string "{myStrn}" is digit string:', myStrn.isdigit())
print(f'Is my string "{myStr}" is digit string:', myStr.isidentifier())
print(f'Is my string "{myStri}" is digit string:', myStri.isidentifier())
print(f'Is my string "{myStrn}" is digit string:', myStrn.isidentifier())     # variable starting with number = invalid

