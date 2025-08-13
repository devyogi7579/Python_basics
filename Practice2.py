# Write a script to read input strings and display output with chars and its index position

#===========================#
# To read input from string
#----------------------------------
readStr=str(input('Enter your string: '))
print('using cnt method')
# Display o/p with Characters and its index position
#----------------------------------------------------
cnt=0
for each in readStr :
    print(f'The characters "{each}" with its index position is : "{cnt}", ')
    cnt+=1
print()
#===========================#
# Another way
#----------------------------------
print('using range method')
readStr=str(input('Enter your string: '))

# Display o/p with Characters and its index position
#----------------------------------------------------
#print(list(range(0,len(readStr))))             # Knowing this is the trick to solve this problem
for eachVal in list(range(0,len(readStr))):
    print(f"The character '{readStr[eachVal]}', with its indexValue is '{eachVal}'")
print()
#===========================#
# Enumerate()
#----------------------------------
print('using Enumerate method')
readStr=str(input('Enter your string: '))
print(list(enumerate(readStr)))