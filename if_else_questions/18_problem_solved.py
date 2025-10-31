# Write a program to check whether a number is divisible by 7 but not by 5.

user = int(input("enter a number"))

if user%7==0 and user %5 !=0:
    print("number is divisible")
else:
    print("false")
    
