# zfill: it adds the zero in left side of string, 
# lets say, string = apple (5 chracters), zfill(10)
myStr='Apple'
print(myStr.zfill(10))  # it will add 5 zeros and 5 apple characters
print(myStr)            # original string as it is

myStr='car'
print(myStr.zfill(10))  # it will add 7 zeros and 3 car characters
print(myStr)            # original string as it is
#======================================================================#
#center: it will bring your string in center place of width choosen

myStr='Python'
print(myStr.center(30))

print(myStr.center(30,'~'))             # fills remianing spaces with *,# or any chracters you want
print(myStr)                            # original string as it is
#print(myStr.center(30,'*','-'))        # Mutli characters not possible
#print(myStr.center(30,'+-'))           # Error: The fill character must be exactly one character long