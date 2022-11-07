import math
def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def mul(x,y):
    return x * y

def div(x,y):
    return x / y

def myfun(x):
    if x > 20:
        x -= 20
    elif x < 10 and x > 5:
        x += 21
    else:
        x *= 2.5 # the original value of x multiplied by 2.5

def func(message, copies=2, name=' Aaron'):# default arguments which will have a base value of 2 and name Aaron if no new argument is introduced
    for i in range(copies):
        print(message+name)
    
# func('Hi', name=' Aaron2') since the function cares about the order you must assign the argument in the func
def SumItems(ListArg):# need to enter a list 
    sum = 0
    for i in ListArg:
        sum += i
        print(sum)
def SumItemsTup(*Args):# puts arguments into a tuple, so can have multiple arguments but cant have another argument in the function after args since it wont ever get there unless its a default arg
    sum = 0
    for i in Args:
        sum += i
    print(sum)
def MinMax(ListArg):
    Min = math.inf
    Max = -1*math.inf
    for i in ListArg:
        if i < Min:
            Min = i
        if i > Max:
            Max = i
    return Min,Max # returns as a tuple
M = MinMax([1.2,2.3,7.1,3.3,1.6])
print(M)     
 
'''
Recursive functions
'''
# doing it iteratively
def pow(x,n):
    result = 1
    for i in range(n):
        result *= x
    return result
print(pow(2,3))
# doing it recursively
def pow2(x,n):
    if (n==1):
        return x
    else:
        return x * pow(x,n-1)
print(pow2(2,3))

def Factorial(Num):
    if Num == 0:
        return 1
    else:
        return Num * Factorial(Num-1)

print(Factorial(5))