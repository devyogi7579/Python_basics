# Memembership operators are very very useful while developing our scripts
# it is to check teh presence and absence of a
    # substring within a given string
    # values within a given list or tuple
    # a key within a given dictionary

# Type of Memembership operators
    # in
    # not in

myStr="I am learning Python"
myList=[3, 'limca', 'coke', 3.5, True]
myTuple=('football', 11, 'Europe', 1965, 'sports')
myDict={'pipeline':['jenkins', 'circle', 'Github Actions'],
        'infra':'Terraform',
        'container':'Docker',
        'cloud':('aws', 'azure', 'gcp')
        }

# search string or characters

print('t' in 'python')
print('T' in 'python')
print('Teaching' in myStr)
print()
print('fanta' in myList)
print('fanta' not in myList)
print()
print(1961 not in myTuple)
print('ansible' in myDict)