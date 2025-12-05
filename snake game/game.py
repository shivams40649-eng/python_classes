'''
1 for snake
0 for gun
-1 for water
'''

computer = random.choice([-1,0,1])
youstr = input("enter your choice:-")
youDist = {"s":1,"w":-1,"g":0}

reverDist = {1:"Snake", -1 : "Water",0: "Gun"}

you = youDist[youstr]

print ("you chose",reverDist[you])
print("Computer chose",reverDist[computer])

if(computer == you):
    print("it's Draw")

elif(computer == -1 and you == 1):
    print("you win")
elif(computer == 1 and you == 0):
    print("you win")
elif(computer == -1 and you == 0):
    print("you Loose!")
elif(computer == 1 and you == -1):
    print("you win!")
elif(computer == 0 and you == -1):
    print("you loose!")
elif(computer == 0 and you == 1):
    print("you Loose!")
else:
    print("Something went wrong")


