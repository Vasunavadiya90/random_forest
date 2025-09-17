def sum(a,b):
    return a+b


def recurssion(n):
    if n==1 or n==0:
        return 1
    else:
        return n*recurssion(n-1)
    
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

def division(a,b,c):
    if a==0:
        print(0)
    return a/b + c

def multiply(a,b,c):
    return a*b*c

def add(a,b,c):
    return a+b+c

def substract(a,b,c):
    return a-b-c
