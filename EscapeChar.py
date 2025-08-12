myStr='Learning "Pyhton" Concepts'
# Single quote doesn't work inside Single quote, but double can work
print(myStr)

#or 

print("Learning 'Python' Concepts")
print()
# Double quote doesn't work inside Double quote, but single quote can

#But to make single or Doble quotes inside single and double quotes we need to use escape characters

print('Working on \'escape\' concepts')
print()
print("Enjoying the working of \"escape\" concepts")
print()
# To print slash
print("Learning 'Python' Concepts \\ and \\ we are good with basics")
print()
# To put the content to new line
print("Learning 'Python' Concepts and \nwe are good with basics")
print()
# to remove the spaces between two words, 
# with \b cursor will come 1 position back, 
# \b\b\b, cursor will come 3 position back and so on
print ("words  are  \b\bseperated  with  two  spaces")
print()
# to overwrite content use \r
# characheters after /r will overwrite the content from 1st position
print('to overwrite the content \r use slash r')
print()
# horizontal tab \t
print("to add\t tab space between \tcharacters")
print()
# verticle tab
print("this will add\v verticle tab space \vbetween words")
