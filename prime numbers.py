a=eval(input("Enter to check whether a number is prime or not:\n"))
s=0
for i in range(1,a):
    if a%i==0:
        s+=1
    elif s==2:
        print("Given number is not a prime number")
        break
        
else:
    print("Given number is a prime number")