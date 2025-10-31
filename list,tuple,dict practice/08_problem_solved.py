#  Merge two lists [1, 2, 3] and [4, 5, 6] without using the + operator.

a =[1,2,3]
b =[4,5,6]

# c = a+b

a.extend(b)
print(a)