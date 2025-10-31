# Write a program to check whether a student has got Distinction, First, Second or Fail.

user = int(input("enter a marks:- "))

if user>=60:
    print("student got first division")
elif user>=45:
    print("student got second division")
elif user>=33:
    print("student got third division")
else:
    print("student fail")

