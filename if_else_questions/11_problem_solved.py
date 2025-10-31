# Write a program to check whether a number is divisible by both 3 and 5

user = int(input("enter a number"))

if(user%3==0):
    print("true")
elif(user%5==0):
    print("true")
else:
    print("false")