# A function is block of code that performs a specific task

def calculateGmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)

def greaterNum(a,b):
    if(a>b):
     print("first number is greater")
    else:
     print("Second number is greater or equal")
    

a = 9
b = 8
"""gmean1 = (a*b)/(a+b)
print(gmean1)"""
 #or
calculateGmean(a,b)
"""if(a>b):
    print("first number is greater")
else:
    print("Second number is greater or equal") """
    #or
greaterNum(a,b)

c = 5
d = 4
"""gmean2 = (c*d)/(c+d)
print(gmean2)""" 
#or
calculateGmean(c,d)
"""if(c>d):
    print("first number is greater")
else:
    print("Second number is greater or equal")"""
#or
greaterNum(c,d)