# pass: When we are not sure, what code we have to write, and to avoid getting errors then we use 'pass'.
# its a placeholder for future code
# The continue and break are used to alter the execution of loops
# break: it terminates the loop when specified condition is met...
# continue: it goes to next iteration when specified condition is met...
#==========================================================================#

myVal=[5,25,36,91,96]

# if myVal:
#     pass
    # if you dont write anything you will get error,
    # to avoid that use "pass" 
    # pass - using pass here will show above commented line also :)
    # same we can use it for 'for and while' loop and functions...

# for each in myVal:
#     pass

# while True:
#     pass

#--------------------------------------------#
# break 
myVal=[5,25,36,91,96]
for each in myVal:
    print(each)
print('For loop ends')
#-----------------------------------------------------------------#
# now we want to break the loop,when each reaches to 36
print()
print('working of break')
myVal=[5,25,36,91,96]
for each in myVal:
    #print(each) - this will print 36
    if each == 36:
        break 
    print(each)     # this will not print 36
print('For loop ends')

#-----------------------------------------------------------------#
# now we want to continue the loop,when each reaches to 36
print()
print('working of continue')
myVal=[5,25,36,91,96]
for each in myVal:
    # print(each)         # this will print 36
    if each == 36:
        continue 
    print(each)        # this will skip printing 36
print('For loop ends')