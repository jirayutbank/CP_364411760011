"""
Name: Jirayut Jeebjong
ID: 364411760011
Group: MIT421
"""

#5. เขียนโปรแกรมไพธอนเพื่อน าเลขบัตรประชาชนมาบวกันเพื่อท านายดวงชะตาดังนี้
#สร้างฟังก์ชันเพื่อหาผลรวมของเลขบัตรประชาชน โดยใช้ชื่อฟังก์ชั่นว่า sumPID()
#สร้างฟังชั่นชื่อ getFortune() เพื่อท านายดวงชะตา ถ้าเป็นเลขคู่ให้ท านายว่า your fortune is good
#ถ้าเป็นเลขคี่ ให้ท านายว่า your fortune is very good

list = []
a = int(input("function1 : "))
b = int(input("function2 : "))
c = int(input("function3 : "))
d = int(input("function4 : "))
e = int(input("function5 : "))
f = int(input("function6 : "))
g = int(input("function7 : "))
h = int(input("function8 : "))
i = int(input("function9 : "))
j = int(input("function10 : "))
k = int(input("function11 : "))
l = int(input("function12 : "))
m = int(input("function13 : "))
def sumPID():
    ID = a+b+c+d+e+f+g+h+i+j+k+l+m
    print("ผมรวมของเลขบัตรประชาชน คือ ",ID)
sumPID()
def getFortune():
    ID = a+b+c+d+e+f+g+h+i+j+k+l+m
    if ID % 2 == 0:
        print(f"{ID} your fortune is good")
    else:
        print(f"{ID} your fortune is very good")
getFortune()
