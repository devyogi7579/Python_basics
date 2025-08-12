# identity operator are used to check whether two variables/objects are pointing to the same memory location or not
# Return output in Boolean data format

# Types of identity operator
# is     ::::    a is b         # True if both are pointing to same memory location, else false
# is not ::::    a is not b     # True if both are pointing to different memory location, else false

a=[4,5]
b=[4,5]
print(id(a), id(b))
# now check
print(a is b)
print(a is not b)
print()

c=a
d=b

print(id(a), id(c))
print(id(b), id(d))
print()

print(a is c)
print(b is not d)
print()
#=================================================#
# We can also use 'is' and 'isnot'to check the type of variables

print(type(a) is list)
print(type(a) is tuple)
print(type(b) is not list)
print(type(b) is not tuple)
print()
#=================================================#
# This is not gaurnteed
x=5
y=5
print(id(x), id(y))
print()

# But this is gaurnteed
x=15
y=x
print(id(x), id(y))

