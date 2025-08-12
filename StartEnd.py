#The startswith() method returns TRUE, if the string "starts with" the specified prefix (a char or substring), 
# otherwise FALSE
# Syntax: str.startswith(prefix,start,end)
#The endswith() method returns TRUE, if the string "ends with" the specified prefix (a char or substring), 
# otherwise FALSE
# Syntax: str.endswith(suffix,start,end)
myStr='www.amazon.com'
print(len(myStr))
print(myStr.startswith('w'))                #single char, True
print(myStr.startswith('WWW'))              #string, False
print(myStr.startswith('amazon',4))         #string amazon starting with index value 4, True
print(myStr.startswith('amazon',4,15))      # between 4 to 15, is there amazon word, TRUE
print()
print(myStr.endswith('www'))                #False
print(myStr.endswith('m'))                  #True
print(myStr.endswith('zon',5,13))           #False
print(myStr.endswith('zon',7,10))           #True - - - Exact index needed to get TRUE response, else FALSE


