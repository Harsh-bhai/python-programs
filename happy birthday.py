letter='''\tHi name\n
\t“Count your life by smiles, not tears. Count your age by friends, not years.\n
 \tHappy birthday!”\n
 \tI hope all your birthday wishes and dreams come true.\n
\tCongratualtions on your no. th birthday\n
\tHave great day'''
q= input("Name of the birthday Boy/Girl :")
r=input("Enter Age :")
# f=input("Enter your name : ")
c=input("Enter your relation with Harsh (like friend/brother/son etc)")
letter=letter.replace("name",q.capitalize())
letter=letter.replace("no.",r)
print("===============================================================")
print("===============================================================")
print(letter)
print("By your lovely",c,"Harsh Dewangan")
input("PRESS ENTER TO EXIT")

# from playsound import playsound
# playsound("D:\\Harsh\\vscodes\\happy.mp3")
# playsound("D:\\Harsh\\vscodes\\oldhbd.mp3")