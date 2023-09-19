class Vec2d:
    def __init__(self,i,j):
        self.icap=i
        self.jcap=j
class Vec3d:
    def __init__(self,i,j,k):
        self.icap=i
        self.jcap=j
        self.kcap=k
    def __str__(self):
        return f"{self.icap}i {self.jcap}j {self.kcap}k"
a=Vec2d(1,2)
b=Vec3d(1,2,3)
print(a)
print(b)