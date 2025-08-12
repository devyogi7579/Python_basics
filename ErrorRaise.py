# Raise exception handling
# Insteading of displaying error in a clean and formal way we want user to pay attention to the details of error
# for that we have raise exceptions
# Syntax
#   raise Exception("Custom Message")
# Script stops or halt after encountering raise message...
# focus on printing of # print('Our Script Ends Here'.center(50,"-"))
# We can also pass existing exceptions with custom message

try:
    readNum=int(input('Enter any number between 1 to 5: '))
    EnteredNum=range(1,6,1)     # here 0 is out of range
except ValueError:
    print('Input must be an integer')
else:  
    if readNum == 1:
        print(f"Entered number '{readNum}' in word is : one")
    elif readNum == 2:
        print(f"Entered number '{readNum}' in word is : two")
    elif readNum == 3:
        print(f"Entered number '{readNum}' in word is : three")
    elif readNum == 4:
        print(f"Entered number '{readNum}' in word is : four")
    elif readNum == 5:
        print(f"Entered number '{readNum}' in word is : five")
    else:
        print('Entered Num is not in range of [1-5]')        
# Normal error message, does not grab users attentions

#========================================================================#
try:
    readNum=int(input('Enter any number between 1 to 5: '))
    EnteredNum=range(1,6,1)     # here 0 is out of range
except ValueError:
    print('Input must be an integer')
else:  
    if readNum == 1:
        print(f"Entered number '{readNum}' in word is : one")
    elif readNum == 2:
        print(f"Entered number '{readNum}' in word is : two")
    elif readNum == 3:
        print(f"Entered number '{readNum}' in word is : three")
    elif readNum == 4:
        print(f"Entered number '{readNum}' in word is : four")
    elif readNum == 5:
        print(f"Entered number '{readNum}' in word is : five")
    else:                   #This grab users attentions
        raise Exception ('Entered Num is not in range of [1-5]')
        #raise ValueError ('Entered Num is not in range of [1-5]')      # Existing exception with custom message
print('Our Script Ends Here'.center(50,"-"))