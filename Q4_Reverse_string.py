#making two variables to store input and output strings

inp_string=input("Enter a string: ")
otp_string=""

#introducing a for loop to iterate letters present in this variable
for letter in inp_string:
    otp_string = letter + otp_string

print("Reverse of String is : {otp_string}")