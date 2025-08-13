#Enumerate.py
#-------------------
# On enumerate function if you apply list or tuple, you will going to get list and tuple...
# Inside lisst or tupple we have COLLECTION OF TUPLE...
# Syntax:
    # enumerate(string/list/tuple/dictionary/range/anyIterableObject)
# On dictionary we dont apply enumerate function...
# WHY? bcoz we already have method dictionary.items(), which gives both Key and Values

# we can use for loop with enumerate function,
# Only thing to remember here is we need to take two Variables
for I,V in enumerate('Python'):
    print(f'{I} {V}')

print()
#-------------------
readStr=str(input('Enter your string: '))
for IndxVal,Value in enumerate(readStr):
    print(f'{Value} {IndxVal}')

print()
#-------------------
x='Python'
print(enumerate(x))
print(list(enumerate(x)))
# You are getting a list where each value is tupple,
# which consists of index and value for that string
# We can convert list into tuple
# tuple(enumerate(x))
#------------------------
# Inside list we have tuple and inside tuple also we have tuple only
# Inside tuple we have Index and values
# the  same logic can be applied in practice 2 excercise...