# import pygame

class Students:

    def __init__(self, name, Class, marks, age):
        self.name = name
        self.Class = Class
        self.marks = marks
        self.age = age

    __harsh=122

    def printDetails(self):
        return (f'''Name is {self.name}\nClass is {self.Class}\nMarks is {self.marks}\nAge is {self.age}\n ''')

    # harsh=Students("Harsh",12,567,18)
    # print(harsh.printDetails())

    @classmethod
    def from_str(cls, string):
        # a = string.split()
        # for i in a:
            return cls(*string.split())
    
    def __add__(self ,other):
        return self.marks + other.marks   #operator overloading
        
    

class programmer(Students):
    pass

# s=input("Enter string for karan :")
# karan = Students.from_str(s)


# print(karan.name)
# print(karan.printDetails())
# rohan=programmer.from_str("kunal 12 4 35")
# print(rohan.printDetails())
# print(rohan._Students__harsh)
harsh=Students("harsh",12,83,18)
shubham=Students("Shubham",12,34,18)
print(harsh+shubham)
input("Enter enter to exit")

    
 