myStr='Ben Stokes'
lengofmyStr=len(myStr)
print(myStr,)

# Now we want detailed printing of our output like
print('Our string is :', myStr,'and its length is :', lengofmyStr)
print('Our string is:',myStr,'and its length is:',lengofmyStr)

# C-style string formating, if you know C then its ok or leave it
# %s for string
# %d for integers 
# and write all your printing variables inside % like
# '%s and %d are in quotes' and %(all variables are inside round parenthesis)
print('c-style printing')
print('Our String is: "%s" and length of our string is: "%d"' %(myStr,lengofmyStr))

# format method
# "{} {}".format(var1, var2)
print()
print('printing using format method')
print("Our String is: '{}' and length of our string is: '{}'".format(myStr,lengofmyStr))

# F-string
# F or f will work
# print(f'your message : {variable1}'and your message2 : {variable2}')
print()
print('f-style printing')
print(f'Our string is: "{myStr}" and Length of our string is: "{lengofmyStr}"')

# We will use f string only, it is availble from 3.6 version
# we can store the output of fstring into variable and then print it, like
print()
myOutput=(f'Our string is: "{myStr}" and Length of our string is: "{lengofmyStr}"')
print(myOutput)

# output works with or without quoting


