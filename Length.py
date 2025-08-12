# Length is a Function, represented as len()
print()
# to measure length
len('String')
# but did you print?
# To print the output
print(len('String'))                #6
print(len('length of string'))      #16

# Storing output of length function into variable
Article='Docker helps developers bring their ideas to life by conquering the complexity of app development. Actively used by millions of developers around the world, Docker Desktop and Docker Hub provide unmatched simplicity, agility and choice.'
Article_length=len(Article)
print(Article_length)

# Length function works with string only, doesnot work with integers
# myStr=10
# print(len(myStr))
# TypeError: object of type 'int' 

myStr='10'
print(len(myStr))       # this will work bcoz anything quoted in '' is a string or

mystrr=456
print(len(str(mystrr))) # type int converted into type str