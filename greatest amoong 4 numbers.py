a=input("Enter sentence for checking  :")
s="  "
d=" "
q=a.find(s)
if q==-1:
    print("Double spaces not found")
else:
    print("Double spaces found at ",q+1,"th character")
    a=a.replace(s,d)
print("Here is the correct sentence")
print(a)
from playsound import playsound
playsound("D:\\Harsh\\vscodes\\marioend.mp3")
input("press ENTER to exit")