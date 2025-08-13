file=['demo','test', 'log', 'job','tools']
# #for each in file:
# #    print(each)
#----------------------------------
# While printing lets add extensions behind each file, using concat
# #for each in file:
#  #   print(each+'.py')
#----------------------------------
# Now lets store each newly created item in list
# create an empty list
Newfilelist=[]
# # then append it
# for each in file:
#     Newfilelist.append(each+'.py')

# print(Newfilelist)
# In new file we have extension.py
#----------------------------------
# Now in our above for loop we have ONLY ONE block of code, then in this case
# we can write your for loop in one line like

for each in file: Newfilelist.append(each+'.py')

print(Newfilelist)
print()
##===========================================================##
# to perform same one operation in each value of list... then we can write same above block of code like this

#file=[each+'.py' for each in file:]
file=[each+'.py' for each in file]      # without: it works
print(file)

##===========================================================##
#Remember this, ITs a special case of using for loop, where we modify the exisiting value of list items
# Opertion performed: adding file extensions to all list items
#Syntax:
    # file=[each'Operation' for loop]
    # file=[each+'.py' for each in file]
# Explore what other operations we can perform with this specail case of using for loop
# There are many operations you can perform on a list of filenames (or any strings) using a for loop in Python.
# Here are several common operations you can do with the `file` list:

### 1. **Removing extensions (instead of adding)**
file = [each.replace('.py', '') for each in file]  # Remove .py extension if present

### 2. **Changing case (uppercase/lowercase)**
file = [each.upper() for each in file]  # Convert to uppercase
file = [each.lower() for each in file]  # Convert to lowercase

### 3. **Replacing parts of filenames**
file = [each.replace('old', 'new') for each in file]  # Replace 'old' with 'new'

### 4. **Adding prefixes**
file = ['prefix_' + each for each in file]  # Add a prefix

### 5. **Extracting specific parts (e.g., first 5 characters)**
file = [each[:5] for each in file]  # Take first 5 characters

### 6. **Splitting filenames (e.g., by underscores)**
file = [each.split('_')[0] for each in file]  # Take the part before first '_'

### 7. **Filtering filenames (e.g., only those starting with 'a')**
file = [each for each in file if each.startswith('a')]  # Keep only filenames starting with 'a'

### 8. **Getting the length of each filename**
file_lengths = [len(each) for each in file]  # List of lengths

### 9. **Checking if a substring exists**
has_test = ['test' in each for each in file]  # List of True/False

### 10. **Stripping whitespace**
file = [each.strip() for each in file]  # Remove leading/trailing whitespace

### 11. **Adding counters or indices**
file = [f"{i}_{each}" for i, each in enumerate(file)]  # Add index as prefix

### 12. **Conditionally modifying filenames**
file = [each + '.py' if not each.endswith('.py') else each for each in file]  # Add .py only if missing

### 13. **Joining with paths (using `os.path`)**
import os
file = [os.path.join('folder', each) for each in file]  # Prepend a directory path

### 14. **Removing duplicates**
file = list({each: None for each in file}.keys())  # Deduplicate (Python 3.7+)



