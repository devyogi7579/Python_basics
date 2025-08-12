# split(), rsplit() and splitlines() methods on python strings
# all these three methods return output as a list of values from a given string
# split means divide, default: based on White Space characters or required: split seperator, if required

# string converst into list
myStr='I am Learning Python 3.12.3'
print(myStr.split())
# output = ['I', 'am', 'Learning', 'Python', '3.12.3'] # based on space division is created
print('This is also a way to convert your string into list'.split())

# To convert string into list use any special character in (-:~!@#$%^&*()_=+)
print(myStr.split(':'))     # output:['I am Learning Python 3.12.3']
print(myStr.split('-'))
print(myStr.split('&'))
print(myStr.split('@'))

# Split based on desired characters
myStr='How to split my string based on t character'
print(myStr.split('t'))
# output: ['How ', 'o spli', ' my s', 'ring based on ', ' charac', 'er']
# another way
print(myStr.split(sep='t'))
# decide number of splits
print(myStr.split(sep='t', maxsplit=2)) # spliting will starts from left to right

# Split based on desired string
myStr="I need to go to the store to buy some groceries."
print(myStr.split(sep='to'))
#=================================================================================#
# to achieve spliting in reverse (right to left) use rsplit
# rsplit()

myStr="I need to go to the store to buy some groceries."
print(myStr.rsplit(sep='to', maxsplit=1))
#=================================================================================#

# splitlines()
# to convert your lines into list
myStr="I need to go \nto the store to \nbuy some groceries."
print(myStr)
print(myStr.splitlines())           #without metioning split character '\n'
print(myStr.splitlines('\n'))       # with defining split character '\n'
print()
myStr="I need to go\t to the store to\t buy some groceries."
print(myStr)
print(myStr.splitlines())           #This doesnt worked out  # without metioning split character '\t'
print(myStr.splitlines('\t'))       #This doesnt worked out  # with defining split character '\t'
print()
myStr="I need to go\v to the store to\v buy some groceries."
print(myStr)
print(myStr.splitlines())           # Perfectly worked      # without metioning split character '\v'
print(myStr.splitlines('\v'))       #This worked something different    # with defining split character '\v'


