#index() method is used to get the index of a given chracter or sub-string from a given string
# dont get confused with index values

# 1. index() will give you index value
#--------------------------------------------
myStr='My Python3 version is 3.12.3'
print(myStr.index('Python'))             # will return index value as 3
print(myStr.index('3.12.3'))             # will return index value as 22
#print(myStr.index('5'))                 # ValueError: substring not found
print(len(myStr))                        #28
print(-len(myStr))                       #-28
print(myStr.index('M')-len(myStr))
# index () searches from left to right
print(myStr.index('o')) # this will return 1st o from left, which is at 7th position
# to get 'o' in the range of 10 to 28 characters, we can use
print(myStr.index('o',10,20))   #on 16th position you have another o

# to serch from right to left, we uses rindex() like
print(myStr.rindex('o'))    #16th position from right, which is same as above
#position value is counted from left to right, ie 16th position

#print(myStr.index('o',1,7)) # we know 1st "o" position is 7 but if index() dont find it in that range then 
# it throws error "substring not found"

# 2. To overcome this we can prefer find method
#--------------------------------------------------#
#print(myStr.find('o',start_index,end_index))
print()
print(myStr.find('o',1,5))
# it will thorw -1 instead of error,
print(myStr.find('o',1,10)) # now it is howing 7th position

# we can also use rfind to search from right
print(myStr.rfind('o'))     #16, means 1st o from right is at 16th position

#--------------------------------------------------#
# 3. Count: It gives how many timesyou have that character in the string

print(f'How many times we have character o:',myStr.count('o'))       #2 times
print(f'How many times we have character n:',myStr.count('n'))       #2 times
print(f'How many times we have character 3:',myStr.count('3'))       #3 times
print(f'How many times we have character 3:',myStr.count('3',7,20))       #1 times
print(f'How many times we have String "version":',myStr.count('version'))       #1 times




