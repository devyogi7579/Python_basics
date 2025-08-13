# For loop:
# Syntax:
    # for each in string/list/tuple/dictionary/range :
        #logic1         # Block of code
        #logic2         # Block of code
        #logic...n      # Block of code
# Remember two points about for loop
    #1. each is a variable
    #2. For loop is not an infinite loop like a while loop, # lopp will run for n number of times
        # n=len(string/list/tuple/dictionary/range)
#=======================================================================#
print(1, 'String')
for each in "Python":
    print('Welcome to the  world of python')
print()
#or
print(2, 'String')
for each in "Python":
    print(f'The characters in "Python" are: {each}')
print()
#or
print(3, 'String')
myStr="Python"
for each in myStr:
    print(f'The characters in "Python" are: {each}')
print()
#=======================================================================#
print(4, 'list')
myList=['Python', 'Go', 'Shell Scripting']
for eachVal in myList:
    print(f'For Automation DevOps Engg must know: {eachVal}')
print()
#=======================================================================#
print(5, 'tuple')
myTuple=('Git', 'Docker', 'Jenkins', 'K8s', 'TF', 'Ansible')
for eachVal in myTuple:
    print(f'Tools DevOps Engg must know: {eachVal}')
print()
#=======================================================================#
print(6, 'dictionary')
myDict={
    'VersionControl':'Git',
    'Build':'maven',
    'ContainerMgt':'Docker',
    'infraMgt':'TF',
    'ConfigMgt':'Ansible'
}
# By default, iterating over a dictionary gives you its keys:
print('Default printing')
for eachVal in myDict:
    print(f'Tools DevOps Engg uses : {eachVal}')
print()
# Explicitly to gets keys
print('Explicitly to gets keys')
for eachVal in myDict.keys():
    print(f'Tools DevOps Engg uses : {eachVal}')
print()
# Explicitly to gets values
print('Explicitly to gets values')
for eachVal in myDict.values():
    print(f'Tools I know how to use : {eachVal}')
print()
# Explicitly to get both keys and values
print('Explicitly to get both keys and values')
for eachKey,eachVal in myDict.items():
    print(f'Keys: {eachKey}, \tValues: {eachVal}')
print()

#=======================================================================#
print(7,'range')
for eachRange in range(0,6):
    print(f'{eachRange}')
print()
#=======================================================================#
# some important points
#There is No output---AND ther is No errors--- this is important
# if string is empty For loop never execute the block of code
print(8,'emptyString')
for eachChar in '':
    print(f'The characters are: {eachChar}')
#-----------------------------------------------------#
print('Emptylist')
for eachlist in []:
    print(f'The characters in list are: {eachlist}')
#-----------------------------------------------------#
print('Emptytuple')
for eachtup in ():
    print(f'The characters in tuple are: {eachtup}')
#-----------------------------------------------------#
print()
for eachdict in {}:
    print(f'The characters in dictionary are: {eachdict}')
print()
#=======================================================================#
# Not iterable - integer/Boolean/None
#-----------------------------------------------------#
# print()
# for eachint in 5:       #TypeError: 'int' object is not iterable
#     print(f'The num is: {eachint}')
# print()
#-----------------------------------------------------#
# print()
# for eachbool in True:   #TypeError: 'int' object is not iterable
#     print(f'The Boolean is: {eachbool}')
# print()
#-----------------------------------------------------#
print()
for eachnone in None:   #TypeError: 'NoneType' object is not iterable
    print(f'The none: {eachnone}')
print()
#=======================================================================#