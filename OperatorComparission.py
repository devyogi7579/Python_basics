# Comparission operators are used to compare two values of same types (strings or numbers)
# Comparission operators cannot be used to compare one string and one number
# Result of two comparission is always True or False (Boolean Data)
print()
print(5<9)
print(5>9)
# or
print()
a=5; b=9
print(a>b)
print(a<b)

# Operator          Examples            Meaning
#-----------------------------------------------------------
# >                 x>y                 True if operand is greater than 
# <                 x>y                 True if operand is Lesser than
# ==                x==y                True if operands are equal
# !=                x!=y                True if operands are not equal
# >=                x>=y                True if operands are greater than or equal
# <=                x<=y                True if operands are lesser than or equal

# comparassion of STRINGS
print()
print('a' < 'b')
print('Apple'=='Mango')

# Why for strings python compares the ASCII values
# to get ASCII values there is a order function 
print()
print(ord('a'), ord('b'))
# print(ord('Apple'), ord('Mango'))     # TypeError: ord() expected a character, but string of length 5 found
