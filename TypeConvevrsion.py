#!/usr/bin/python3

# type integer
x=5        
print(x, type(x))
print()
#5 <class 'int'>

# type float
y=9.81
print(y,type(y))
print()
#9.81 <class 'float'>

# type string
z='apple 16'                        # anthing inside quotes become string
print(z, type(z))
print()
#apple 16 <class 'str'>

#newZ=int(z)                     # this will throw error invalid literal
#print(newZ, type(newZ))
# Why, bcoz we cannot convert pure string into integers, as int assumes number system with base 10
# ValueError: invalid literal for int() with base 10: 'apple 16'

# integer to string
newX=str(x)                     # this is possible
print(newX, type(newX))
print()
#5 <class 'str'>

#such strings can be converted back into integers
newInt=int(newX)
print(newInt, type(newInt))
#here integer system assumes that whatever you have provided is having base system 10
# 10 in binary system is 2
# 100 in binary system is 4
print()
#5 <class 'int'>

# float to integer
Newy=int(y)
print(Newy,type(Newy))
print()
#9 <class 'int'>, 9.81 gets converted into float

# integer to float
newFloatx=float(x)
print(newFloatx, type(newFloatx))
print()
#5.0 <class 'float'>

