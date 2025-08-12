# if elif...else Conditional statements

# Read any number between 1 to 5 and display the given numbers in words

readNum=int(input('Enter any number between 1 to 5: '))
EnteredNum=range(1,6,1)

# if readNum in EnteredNum :
#     print(f"Entred Number {readNum} is in range of {EnteredNum}")
# else:
#     print(f"Entred Number {readNum} is not in {EnteredNum}")

#if readNum == EnteredNum:      This logic doesnt work
if readNum == 1:
    print(f"Entered number '{readNum}' in word is : one")
else:
    if readNum == 2:
        print(f"Entered number '{readNum}' in word is : two")
    else:
        if readNum == 3:
            print(f"Entered number '{readNum}' in word is : three")
        else:
            if readNum == 4:
                print(f"Entered number '{readNum}' in word is : four")
            else:
                if readNum == 5:
                    print(f"Entered number '{readNum}' in word is : five")
                else:
                    if readNum not in EnteredNum:
                        print('Entered Num is not in our range')
print()
#====================================================================================#                        
# instead of passsing if-else statement as above we can pass it as if -elif -elif
# Syntax is
'''
if expression 1:
    logic-1
    logic-2
    logic-n
elif expression 2:
    logic-1
    logic-2
    logic-n
elif expression 3:
    logic-1
    logic-2
    logic-n
else            # else block of code is optional, otherwise can be skipped
                # else is used if all expressions are FALSE
    logic-1
    logic-2
    logic-n
# If all 03 blocks of elif are true then first block of code is executed FIRST
'''
readNum=int(input('Enter any number between 1 to 5: '))
EnteredNum=range(1,6,1)
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
    print('Entered Num is not in our range')
print()
#====================================================================#
# Another shortcut

NumDict={
    1:'One',
    2:'two',
    3:'three',
    4:'four',
    5:'five'
}
if NumDict.get(readNum):                                
# from this expr we will get some o/p, which is TRUE
# for num not in range, get will return NONE, which is FALSE
    print(f'Entered Number is: {NumDict.get(readNum)}')
else:
    print('Sorry!!! Entered Num is not in our range')