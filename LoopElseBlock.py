# else block wont execute when break executed 
# and else block is independednt from continue
print('for loop and else block without break')

for i in range(1,6):
    print(i)
else:
    print('End of for loop')
#-----------------------------------------#
print()
print('for loop and else block with break')

for i in range(1,6):
    if i==3:
        break
    print(i)
else:
    print('End of for loop')
# with break else block wont get executed
#-----------------------------------------#
print()
print('for loop and else block with continue')

for i in range(1,6):
    if i==3:
        continue
    print(i)
else:
    print('End of for loop')
# with continue else block get printed