# Strip removes white spaces. 
# Default white spaces are "Space ' ', newline '\n', tab space '\t', carriage return '\r'"
# strip() : will remove matching charachers from both sides
# lstrip() : will remove matching charachers from left sides
# rstrip() : will remove matching charachers from right sides

myStr='i-phone'
print('Original String with no white spaces:',myStr)
print('Resulted String:',myStr.strip())
print()

myStr='    i-phone 16'
print('Original String with left white space:',myStr)
print('Resulted String:',myStr.lstrip())
print()

myStr='\n\t\r\v  i-phone 16\n\t\r\v'
print('Original String with multiple white space:',myStr)
print('Resulted String:',myStr.strip())
print()

myStr='www.python.org'
print('Original String:',myStr)
# to remove characters, it starts with left to right
print('Resulted String:',myStr.strip('o'))  # to remove 'o, r, g' we need to give char near o like rg or h or n
print('Resulted String:',myStr.strip('w'))  # this will remove all 'w'
print('Resulted String:',myStr.strip('.g')) # this will remove g near .
print('Resulted String:',myStr.rstrip('g')) # this will same job as above
print('Resulted String:',myStr.strip('.org')) # this will remove  exact .org
print()

mystrr='www.random360.com'
print('Original String:',mystrr)
print('Resulted String:',mystrr.strip('w.''.com'))  #this will strip from both side
print('Resulted String:',mystrr.strip('w.''360''.com')) # this  doesnt goes as expected
print('Resulted String:',mystrr.rstrip('w.''.com')) # left side www. is not removed
print('Resulted String:',mystrr.lstrip('w.''.com')) # right side .com is not removed
print('Resulted String:',mystrr.strip('w.''.com'))
print()


