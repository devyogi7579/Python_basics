# Nested Loop: Loop inside a loop

# We have to display strings with its asci code

myStr='Python'
for each in myStr:
    #print(each)         # This will print all characters of string
    #print(ord(each))    # to print asci code we have
    print((each), ord(each))

# Similar if we want to do with loops, then we need to use Nested loops
print()
myList=['Python','Go','Bash']

for eachitem in myList:
    print(''.center(60,"-"))                     # for decoration purpose
    print((eachitem))
    print(''.center(60,"-"))                     # for decoration purpose
    for each in eachitem:
        print((each), ord(each))
                     
print('End of Nested for loop'.center(60,"-"))

