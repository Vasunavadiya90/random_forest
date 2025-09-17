def sum(a,b,c):
    return a+b+c


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

def division(a,b):
    return a/b