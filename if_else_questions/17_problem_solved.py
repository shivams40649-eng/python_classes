# Write a program to check whether a given year is a century year (like 1900, 2000)

user =int(input("enter a year"))

if user%100==0:
    print("this is a century year")
else:
    print("not century year")

