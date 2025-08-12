# if and if-else conditional statements
# Syntax:
    # if conditional statement :            # : is very important
    
    # if expression :
    # if[1 space is must] expression[optional to give space]:
        #logic -1       # Block of code
        #logic -2       # Block of code
        #logic -n       # Block of code

# Expression can be framed with any operator or
# with combination of multiple operators, 
# only condition is expression result be either True or False - simply Boolean Data
# For EMPTY (string/list/tuple/dictionary/0 (zero)/false/None)----> Result is always False only
# For Non EMPTY (string/list/tuple/dictionary/(Non zero)/True)----> Result is always True only
# For Block of code, we must give indentation --- 1 spaces or 4 spaces, choice is yours
print()
#if '' :            #Empty string
#if False :         #False
#if 0 :             #Zero Num
#if () :             #Empty Tuple
#if [] :            #Empty List
#---------------------------------------
#if 'Hello' :           #some string
#if True :              #True
#if -3 :                  #Non Zero Num
# #if (3, 'Hi') :                #Non Empty Tuple
# if [3, 'Hi'] :                #Non Empty List
#     print('We are you good at variables')
#     print('We are you good at string operations')
#     print('We are you good at list/tuple/dict operations')
#     print('We are you good at operators')
#     print()
# print('****Thank You-Keep Learning****') 

#=========================================================================#

myToolVersion={
    'Docker':'24.01.25',
    'Git':'2.50.1',
    'Ansible':'2.19.25'
}
# Docker!=DOCKER

usrReqTool=input('Enter your tool name and I will give you its version: ')
if usrReqTool in myToolVersion :        # : with space
    ToolVersion=myToolVersion.get(usrReqTool)
    print(f"Your entered tool is '{usrReqTool}' and its version is: '{ToolVersion}'")
else:                                   # : without space
    print(f'Tool Name is in TitleCase, please enter name correctly or \nTool is not available in the list')