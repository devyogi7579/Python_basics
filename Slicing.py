# Slicing: Extracting string or single character from a string
# Concept of STEP: 
# step=(2nd value - 1st value) when we read Left to right
# if step = +ve, then direction is L to R
# if step = -ve, then direction is R to L
# if step is known then we can determine the 1st value or 2nd value, depends on what is knowns

# step      #possible values starting from 0            or from -2 are
#   1       0+1=1, 1+1=2,3,4 and so on                  -2+1=-1, -1+1=0, 0+1=1,2,3 and so on
#   2       0+2=2, 2+2=4, 6,8 and so on                 -2+2=0,0+2=2,4,6,8 and so on
#   -1      0-1=-1, -1-1=-2, -2-1=-3,-4,-5 and so on    -2-1=-3,-4-5 and so on
#   -2      0-2=-2, -2-2=-4,-4-2=-6,-8 and so on        -2-2=-4,-6,-8,-10 and so on
#==================================================================================================#
# Slicing single char: 
# myStr[indexNumber]    ---> will give character for given indexNumber (+ve/-ve)
# Slicing multiple char:
# myStr[StartIndx:EndIndx:Step]  meaning myStr[range:Step]
# +ve step means {left to right} slicing of string
# -ve step means {right to left} slicing of string
# step not mention means step = (+ve)1, 
# if step is +ve then startIndex = 0 [Remember this]
# if step is -ve then default startIndex is -1
# Default endIndex is infinity (+ve/-ve) wrt starting index

# if index range and step is in same direction(irrespective of +ve or -ve)===You will going to get output
# if index range and step is in OPPOSITE direction(irrespective of +ve or -ve)===You will not going to get output
# so to gt output, you need to make sure to maintain range and step in the same direction
#### slicing is done Just before endIndex and not till the endIndex, based on string step ####
#==================================================================================================#

myStr="Python-3.X.x"
# P=0|y=1|t=2|h=3|o=4|n=5|-=6|3=7|.=8|X=9|.=10|x=11|                    +ve indexing
# P=-12|y=-11|t=-10|h=-9|o=-8|n=-7|-=-6|3=-5|.=-4|X=-3|.=-2|x=-1|       -ve indexing
print(len(myStr))
print(myStr[3:6:1])     # 3 4 5 | 6         #slicing is done Just before endIndex and not till the endIndex
print(myStr[-7:-3:1])   # -7 -6 -5 -4 |-3   #slicing is done Just before endIndex and not till the endIndex
#print(myStr[-3:-8:1])   #-3 -2 -1          # No output you will get, it will throw error
print(myStr[-3:-5:-1])  #-3, -4 | -5
print(myStr[2:7:3])     #2, 5 | 8 11
print()
print(myStr[2:])                            # startIndex=+ve, no end Index means infinity and step = 1
# this will print all characters from 2nd Index ie t to x
print(myStr[2:7])                           # No step means step = 1
# this will print all characters from 2nd Index to 6th index ie 2 3 4 5 6 | 7
print(myStr[::])                            # No start,end Index without step, then this will print entire string as it is, why
# No step means, step =1, and starting index = 0, then 0+1=1,2,3 and till the last index,which is 12
print(myStr[::-1])                          # -ve means R to L, if Step = -1, then startIndex = -1 and end Index = -inifinity
# -1+(-1) = -2 +(-1)=-3 and till -12
#-1=x, -2=., -3=X and till -12=P
# Your complete string will get in reverse order