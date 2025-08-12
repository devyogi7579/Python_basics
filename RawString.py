#myPath='D:\LearningPython\new'
#print(myPath)
# this will throw SyntaxWarning: invalid escape sequence '\L', 
# \n is a escape character, so its a good practice to use \\

myPath='D:\\LearningPython\\new'  
print(myPath)
# instead of using \\, use r or R outside of '' quotes
myPath=r'D:\LearningPython\new'  
print(myPath)
myPath=R'D:\LearningPython\raw\string'  
print(myPath)

#In Ubuntu you wont face problem of \, but we will use Regexp where we use \. for literals, we will see
# at the time of learning literals
