#we will use a for loop to compute.
def factorial(n):

#initializing the variable 'factorial'
    factorial =1

#including a for loop to the range function ie;
    for i in range(n):
        factorial*=i+1

    return factorial

#test
print(factorial(5))