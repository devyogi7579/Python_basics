# Logical operators
    # Very imp operators to develop our scripts
    # LO are useful to combine and validate 
    # multiple comparison, 
    # identiy (is/is not)or 
    # membership operators (in/not in)
# end
# We will dicuss about multiple comparison operators (>, <, <=, >=, ==, !=) only

# We have 03 types of logical operators
    # and
    # or
    # not
# end

# which is greater amongst 2 4 6, how to prove it logially
#   when 6 > 2  True
#   when 6 > 4  True
# when both situations are true then its TRUE
# best practice, provide your expression in ()
print((6>4) and (6>2))      # output will be True

# truth table
#--------------------------------------------------------------------------------
# T and T   True            T or T   True
# T and F   False           T or F   True
# F and T   False           F or T   True
# F and F   False           F or F   False

# Operator      Syntax          Description
#---------------------------------------------------------------------------
# and           x and y         True = if both x and y are true
# or            x or y          True = if eiher of x and y are true
# not           not x           if something is True not turns it into false

print((6>9) and (6>2)) 
print()

# OR operator
print((6>9) or (6>2))           #True, if eiher of x and y are true
print((16>9) or (6>2)) 
print((16<9) or (6<2))

# NOT operator, to reverse the actual result we are getting
print()
print(not((16<9) or (6<2)))
print(not((16>9) or (6>2)))