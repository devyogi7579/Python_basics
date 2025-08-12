# Sample practice with data structures
devOpsTool1="maven"
devOpsTool2="docker"
devOpsTool3="jenkins"
devOpsTool4="K8s"
devOpsTool5="git"

#database
database1='oracle'
database2='mysql'
database3='mongodb'

#languages
lang1='python3'
lang2='bash'
lang3='go'
lang4='yaml'

#OS
os1='windows'
os2='linux'

# cloud
cl1='aws'
cl2='azure'
cl3='gcp'

# For all devOps tools we can have one list or one tuple like
devOpsTools=['git', 'maven', 'docker', 'jenkins', 'k8s']
db=['oracle','mongodb','mysql']
lang1=('python3','bash','go','yaml')

# or we can have one dictionary also
dopsTools={"devOpsTools":['git', 'maven', 'docker', 'jenkins', 'k8s'], "db":['oracle','mongodb','mysql'], "lang":['python3','bash','yaml','go']}
# or for better representation we can have

dopsTools={
    "devOpsTools":['git', 'maven', 'docker', 'jenkins', 'k8s'], 
    "db":['oracle','mongodb','mysql'], 
    "lang":['python3','bash','yaml','go']
    }

# to print keys from dictionary
print(dopsTools)
print()
#  to print selected keys from the dictionary
print(dopsTools['devOpsTools'],dopsTools['lang'])
print()
#alternate Option using get()
print(dopsTools.get('devOpsTools'), dopsTools.get('lang'))
print()
#  to print all keys from the dictionary
print(dopsTools.keys())
print()

#  to print all values from the dictionary
print(dopsTools.values())
print()

#==========================================================================#
dopsTools={
    "devOpsTools":['git', 'maven', 'docker', 'jenkins', 'k8s'], 
    "db":['oracle','mongodb','mysql'], 
    "lang":['python3','bash','yaml','go']
    }
# To get 1st lang (value) from dopsTools (Dictionary)
print(dopsTools)                        # prints dictionary
print(dopsTools.get('lang'))            # prints key values for given key from dictionary
print(dopsTools.get('lang')[0])         # prints desired index values for the given key from dictionary
print()

# To print that key which we dont have in our dictionary
print(dopsTools.get('cloud'))           # output = None
#print(dopsTools.get('lang')[5])         # output = IndexError: list index out of range

# to tell index 5 is not a valid index, we need to know
# operator
# conditional statements
# and some looping concepts