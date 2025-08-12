# Python string is nothing but sequence of charachters represented inside quotes
# python gives position to chracters
# Pyhton-3.X.x
# 01234567891011

myStr='Pyhton-3.X.x'
print(len(myStr)) 
# its 12, 
# from left to right its Positive indexing, its starts from 0
# from right to left its negative indexing, its starts from -1
# Note: we can extract any given characters from given length.
                # Syntax: myStr[indexNumber] 
# For the 1st time in python learning we came across square bracket

print(myStr[0])             # results in 'P'
print(myStr[-12])           # results in 'P'
print(myStr[6])             # results in '-'
print(len(myStr)-1)         # this will give length -1 = count only, to get char use []
print(myStr[len(myStr)-3])
print(myStr[-len(myStr)])

# Very important to get 1st and last characters

print(myStr[0],myStr[-1])

