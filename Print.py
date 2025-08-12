#clear is not used to clear the terminal
print() # this will print empty line like echo
print('message')                # single quote
print("Your message")           # Double quote
print("""Your Greetings""")     # Tripple double quotes
print('''Your Wishes''')        # Tripple single quotes
print("'Your Prayers'")        # mix single and double quotes ----- this doesnt work
print('string1','string2','string3',"all are seperated by , which you will not see on terminal")
print('Hi' 'how' 'are' 'you' "all strings are seperated by even spaces but you will get o/p like Hihowareyou")
# point to note here is anything inside ' ' or " " are safe to write like a normal, else you wont get desired output
print()
#observe th output
#print('string1','string2','string3'sep=':') #, between 3 and sep is must, else throws error
print('string1','string2','string3',sep=':')
print('string1','string2','string3',sep=' : ')
print('string1','string2','string3',sep=' / ')
print('string1','string2','string3',sep=' || ')
print('string1','string2','string3',sep=' ? ')
print('string1','string2','string3',sep=' - ')


