def sum(a,b):
    return a+b

def recurssion(n):
    if n==1 or n==0:
        return 1
    else:
        return n*recurssion(n-1)
    
    