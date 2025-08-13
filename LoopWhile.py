# while loop ia used to repeatedly execute a block of code until the condition is satisfied
# if no condition is provided loop will continue to run, infinitely
# loop stops working when condition is false
# When we dont know for how many iterations we have to run the block of code, use while loop
# Syntax:
    # while expression :        # Condition of expression should result in TRUE or FALSE     
        # logic1
        # logic2
#Note: if expression is always true, then it becomes infinite loop
# And for while loop also we have else block, same as for loop
# and else block only execuits, after successful completion of for loop
#==========================================================================#

print('Simple infinite while loop')

# while True:
#     print('I am comfortble with python')

#-------------------------------------------------------#
# print()
# print('Guess the Number')
# print()
# Num=61
# UsrInput=int(input('Enter your Guess number:'))

# if UsrInput == Num:
#     print(f'Congratulation!!!\nYou guessed the number correctly...\nWeldone!!!')
# else:
#     print('Ooopsss, Try Again')
# #-------------------------------------------------------#
# # Now make this block of code to run for 05 times,
# # Means in 05 chances, user should guess the number...
#-------------------------------------------------------#
# print()
# print('Guess the Number')
# print()
# Num=61
# #UsrInput=int(input('Enter your Guess number:'))
# for each in range(0,5):
#     UsrInput=int(input('Enter your Guess number:'))
    
#     if UsrInput == Num:
#         print()
#         print(f'Congratulation!!!\nYou guessed the number correctly...\nWeldone!!!')
#         exit()      # To exit out if user gues the number correctly
#         # Exit will stop the working of remaining script, if you have some code below loop, that wont execute 
#         # Focus on list line, that wont get printed because of exit
#         # Can we give hint to user after 3 chances, i think with break and continue we can achieve this
#     else:
#         print()
#         print('Ooopsss, Try Again')
#         
# print('!!!!!Thank you for playing this game!!!!!')
#-------------------------------------------------------#
# Now make this block of code to run inifinitely
#-------------------------------------------------------#
print('Guess the Number')
print()
Num=61
#var=True
condition=True
while condition:
    print()
    UsrInput=int(input('Enter your Guess number:'))
    
    if UsrInput == Num:
        print()
        print(f'Congratulation!!!\nYou guessed the number correctly...\nWeldone!!!')
        #exit()      # To exit out if user guesses the number correctly
        # Instead of guess we can use Variable that turn into FALSE
        condition=False
    else:
        print()
        print('Ooopsss, Try Again')