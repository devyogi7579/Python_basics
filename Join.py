# Join Method: join()
# joins the  list or tuple and converts them into string, check type
# Condition: All values inside list and tuple must be strings
# syntax:   Define seperator    
# sep""     Empty seperator
# sep" "    Empty seperator
# sep"@@@@"    at the rate seperator
# anything can be passed between quotes

# sep.join(YourVariable)

myList=["I", "Love", "Python", "Scripting", "Its" "very", "easy"]
myTuple=("I", "Love", "Python", "Scripting", "Its" "very", "fantastic")

#sep=""
sep=" "
NewStr=sep.join(myList)
# to see the result, print
print(sep.join(myList),type(NewStr))
print()
NewStr=sep.join(myTuple)
print(sep.join(myTuple), type(NewStr))
print()

# Another way of passing seperator
print('-@-'.join(myList))       # in place of seperator we are passing any special characters
print()
print('$*#'.join(myTuple))
print()

#==================================================================================================#

myStr='I love python scipting'
#replace space with under scores
print('_'.join(myStr))                  #I_ _l_o_v_e_ _p_y_t_h_o_n_ _s_c_i_p_t_i_n_g
#print('_'.join(myStr.split()))          # I_love_python_scipting            ###this is what we are looking for
print('_'.join(myStr.split(sep=' ')))
print()
myNewstr=('_'.join(myStr.split(sep=' ')))
print(myNewstr, type(myNewstr))
