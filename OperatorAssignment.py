a=4
# here = is the assignment
# a=a+3 # then for this we have a shortcut
a+=3                                    #[Operation performed on variable itself]
# so += will become assignment operator
print(a)
print()
#=============================================================#
# Likewise we have different operators
#=============================================================#
# Operator         #Example (shortCuts)             #sameAs 
#----------------------------------------------------------------
# =                 x = 5                           x = 5
x = 5
print(int(x))
print()
#----------------------------------------------------------------
# +=                x += 5                          x = x+5
a = 5
a+=5
print(int(a))
print()
#----------------------------------------------------------------
# -=                x -= 5                          x = x-5
a = 5
a-=3
print(int(a))
print()
#----------------------------------------------------------------
# *=                x *= 5                          x = x*5
a = 5
a*=3
print(int(a))
print()
#----------------------------------------------------------------
# /=                x /= 5                          x = x/5
a = 5
a/=3
print(int(a))
print()
#----------------------------------------------------------------
# %=                x %= 5                          x = x%5     [Modulus]
a = 5
a%=3
print(int(a))
print()
#----------------------------------------------------------------
# //=               x //= 5                         x = x//5    [Floor Division]
a = 5
a//=3
print(int(a))
print()
#----------------------------------------------------------------
# **=               x **= 5                         x = x**5    [Exponential]
a = 5
a**=3
print(int(a))
print()
#----------------------------------------------------------------
# &=                x &= 5                          x = x&5
a = 5
a&=3
print(int(a))
print()
#----------------------------------------------------------------
# |=                x |= 5                          x = x|5
a = 5
a|=3
print(int(a))
print()
#----------------------------------------------------------------
# ^=                x ^= 5                          x = x^5
a = 5
a^=3
print(int(a))
print()
#----------------------------------------------------------------
# >>=               x >>= 5                         x = x>>5
a = 5
a>>=3
print(int(a))
print()
#----------------------------------------------------------------
# <<=               x <<= 5                         x = x<<5
a = 5
a<<=3
print(int(a))
print()
#----------------------------------------------------------------
# walrus Assignment operator (:=) It is useful to assign any variable value in expression itself.
print()
a=5
b=8
sum=int(a)+int(b)
print(sum)

# suppose b value we want to read while exicuting our python script
print()
a=5
b=int(input("Enter your b value: "))
sum=int(a)+int(b)
print(sum)

# Instead of defining your variable b seperately, in the expression itself we can define the variable, 
# and read from cmd line, for this we have to use WALRUs operator (:=)
print()
a=5         
#b=int(input("Enter your b value: "))
sum=int(a)+(b:=int(input("Enter your b value: ")))      #3 ((()))
print(sum)

print()
#a=5         #Constant values like  a can also be defined with walrus operator
#b=int(input("Enter your b value: "))
sum=int(a:=8)+(b:=int(input("Enter your b value: ")))      #3 ((()))
print(sum)
print(a,b)