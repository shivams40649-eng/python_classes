# Write a program to check if a number is single-digit, double-digit, or more

user = int(input("enter the number"))

if user>=1 and user <=9:
    print("this is single digit number")
elif user >=10 and user <=99:
    print("this number is double digit")
else:
    print("more than two digit number")