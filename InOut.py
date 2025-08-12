# note: input read a number as string only
# syntax 
# var=input()                       # Without explaination to user
# var=input('Enter one number: ')   # With explaining user, what to do
myVar='Apple'
myNewvar=myVar
print(f'my variable is: {myNewvar}')
myNewvar=len(myVar)
print(f'my variable length is: {myNewvar}')
print()

num1=input()
num2=input()
print(f'The entered two numbers are "{num1}" and "{num2}".')
print()

a=input('Enter one number: ')
alen=len(a)
b=input('Enter second number: ')
blen=len(b)
print(f'Number entred by users are "{a}" and "{b}" and their lenghts are "{alen}" and "{blen}".')
print()
