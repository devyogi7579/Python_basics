# For loop to read Dictionary Key and Values
myDict={
    'VersionControl':'Git',
    'Build':'maven',
    'ContainerMgt':'Docker',
    'infraMgt':'TF',
    'ConfigMgt':'Ansible'
}

# By default, iterating over a dictionary gives you its keys:
#--------------------------------------------------------------
print('Default printing')
for eachVal in myDict:
    print(f'Tools DevOps Engg uses : {eachVal}')
print()

# Explicitly to gets keys       #myDict.keys()
#--------------------------------------------------------------
print('Explicitly to gets keys')
for eachVal in myDict.keys():
    print(f'Tools DevOps Engg uses : {eachVal}')
print()

# Explicitly to gets values     #myDict.values()
#--------------------------------------------------------------
print('Explicitly to gets values')
for eachVal in myDict.values():
    print(f'Tools I know how to use : {eachVal}')
print()

# Explicitly to get both keys and values        #myDict.items()
#--------------------------------------------------------------
print('Explicitly to get both keys and values')
for eachKey,eachVal in myDict.items():
    print(f'Keys: {eachKey}, \tValues: {eachVal}')
print()
# print each keys and values

for v1, v2 in [(11,16),[24,26],[34,36]]:
    print(f'{v1}\t{v2}')
print()
for v1, v2,v3 in [(14,15,16),[24,25,26],[34,35,36]]:
    print(f'{v1}\t{v2}\t{v3}')