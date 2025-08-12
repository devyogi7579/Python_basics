#!/usr/bin/python3

x=9
y=12.5
print(x)
print()
print(x,y)

print(id(x),id(y))

# To delete a variable which you dont required further in the code use
del x
#print(x) # you will get error like 'x' not defined

# to define multiple variables in single line use semicolan;
l=9;m=15;n=25

# to define same values to multiple variables
a=b=c=8

# to define another variable value to some variable
z=l
print(z)

#Rules to define variable names
# var name can only have alphnumeric characters and underscores (A-Z, a-z, 0-9 or _)
# invalid var name = 8x, it should not start with numbers
# vaild var name = _myNumber=25, startign with underscore
# var name should not have spaces
# var names are case senstitive in nature
a=5;A=6
print(a)
print(A)

# Dont take default key words as  variable names
# use help("keywords") to get a list words which should be avoided to use as a variable names
# or refer to script getDefaultKeywords.py



