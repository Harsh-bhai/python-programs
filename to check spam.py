l=["subscribe","subscriber","support","yesterday","job","mother","GB","cry","ma","maa",
    "money",
    "maa ki umar",
    "funfact",
    "pray",
    "this man",
    "many of life faliures",]
a=input("Enter sentence for checking whether it is a spam or not:\n")
r=a.split()
for i in r:
    if i.lower() in l:
        print("S P A M \nYou are a SPAMMER")
        break
        
        # from playsound import playsound
        # playsound("D:\\Harsh\\vscodes\\marioend.mp3")
        # break
else:
    print("NOT S P A M")
    # from playsound import playsound
    # playsound("D:\\Harsh\\vscodes\\go.mp3")
input("Press ENTER KEY to exit")