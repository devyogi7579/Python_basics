# For loop with else Block
#Syntax: 
    # for each in string/list/tuple/dict/range/anyiterableObject
        #logic1
        #logic2
    #else
        #logic1
        #logic2
# Note: else block will execute after successful compeletion of for loop
#-----------------------------------------------#
print('With else Block')
for each in 'Python':
    print(each)
else:
    print()
    print('Done with Scripting')
#-----------------------------------------------#
print()
print('Without else Block')
for each in 'Python':
    print(each)

print()
print('Done with Scripting')
#-----------------------------------------------#
# Both output is same... then why we need else block
# when we work with continue and break then we will see the difference of using else block