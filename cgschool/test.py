filename = "D:/Harsh/vscodes python/cgschool/student.txt"
f = open(filename, "r")  # make sure to replace '\' with '/' in above string
r = f.read()
a = r.split("\n")
l = len(a)
s="harsh"
for i in range(5):
#     for j in range(1):
#         print(a[i].split()[j],a[i].split()[j+1])
    print(f"my name is{i}")