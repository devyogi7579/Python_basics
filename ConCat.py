myStr1='Python'
print(type(myStr1))
myStr2='Automation'
myStr3='Scripting'
mySpaceVar=''

# concat using +
print(myStr1 + myStr2 + myStr3) # o/p=PythonAutomationScripting, no space
# to add space use, space vairble 
print(myStr1, mySpaceVar, myStr2, mySpaceVar, myStr3)

print('Concat Using f-string')
print()
print(f'{myStr1}{myStr2}{myStr3}')  # No spacing
print(f'{myStr1} {myStr2} {myStr3}')  # Normal spacing
print(f'{myStr1}    {myStr2}    {myStr3}')  # tab spacing
conCAT=f'{myStr1} {myStr3}'
print(conCAT)
print()
# point to note: Only string concatnation is possible, 
# if you want to concat,integer with str then convert it, into string
# str(int)
myVersion=3
print(type(myVersion))
print(myStr1, mySpaceVar, myVersion)                        # Valid
#print(myStr1 + myVersion)                                  # invalid with +
# + doesnot handle concatnation of string and integer 
# But f string handles this
print(f'My Version of {myStr1} is {myVersion}')             # Valid with f string
print()
#Concat of string and float is possible
myVer=3.12
print(type(myVer))
print(myStr1, mySpaceVar, myVer)                            # Valid
#print(myStr1 + myVersion)                                  # invalid with +
print(f'My version of {myStr1} is {myVer}')                 # Valid with f string
print()
# prefer using f string to avoid conversion of int or float conversions into strings



