#defining function fact
def fact(n):

#setting a limit because the function is calling itself
    if(n==0):
        return 1
    return n * fact(n-1)

result=fact(4)
print(result)