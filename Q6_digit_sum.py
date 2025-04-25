#firstly accept users input
number = int(input("Enter number of choice: "))

#now defining a variable to store the sum
total=0

#introducing a while loop for iteration ie we have to keep taking the last digit from the number and add it to the total variable
while number > 0:
    last_digit = number % 10
    total += last_digit
    number = number//10 #to remove the last digit from the number

print("Sum of the digits of your number :", total)