import random
l=[
    "rock",
    "paper",
    "scissors",
]
def func(a,d):
    for i in d:
        if a[0].lower()==i[0]:
            return i


ans="y"
while ans.lower()=="y":
    a=random.randint(0,2)
    print("Welcome to Stone Paper Scissors Game")
    print("====================================")
    print('''Computer's Turn.............
    computer has chosen its choice
    Now Your Turn''')
    q=input('''
    =================================
    ||Rock(r),Paper(p),Scissors(S)||
    =================================
    Enter your Choice\n :''')
    if q==l[a][0]:
        print("Match Draw/Tie")
        print("You chose : ",func(q,l),"\ncomputer chose : ",l[a])
        
    elif q=="r":
        if l[a]=="paper":
            print("Bad Luck! \nYou lost!!")
            print("You chose : ",func(q,l),"\ncomputer chose : ",l[a])
         
        else:
            print("Congratulations!!!!\nYou Won the Game!!!")
            print("You chose : ",func(q,l),"\ncomputer chose : ",l[a])
         
    elif q=="s":
        if l[a]=="rock":
            print("Bad Luck! \nYou lost!!")
            print("You chose : ",func(q,l),"\ncomputer chose : ",l[a])
         
        else:
            print("Congratulations!!!!\nYou Won the Game!!!")
            print("You chose : ",func(q,l),"\ncomputer chose : ",l[a])
         
    elif q=="p":
        if l[a]=="scissors":
            print("Bad Luck! \nYou lost!!")
            print("You chose : ",func(q,l),"\ncomputer chose : ",l[a])
         
        else:
            print("Congratulations!!!!\nYou Won the Game!!!")
            print("You chose : ",func(q,l),"\ncomputer chose : ",l[a])
         
    ans=input("Play Again(y/n)")
input("Press ENTER key to exit")


