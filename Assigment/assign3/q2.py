"""
Name: Jirayut Jeebjong
ID: 364411760011
Group: MIT421
"""

#2. เขียนฟังก์ชันเพื่อยกกำลังสองสมาชิกทุกตัวใน list และ return list ที่เป็นผลลัพธ์จากการยกกำลังสองออกมา กำหนดให้ฟังก์ชันนี้รับ parameter 1 ตัว คือ listA ที่มีสมาชิกเป็นจำนวนใด ๆ
a = int(input("function1 : "))
b = int(input("function2 : "))
c = int(input("function3 : "))
listA = [a,b,c]
power = 2
for i in range(len(listA)):
    print( listA[i],"ยกกำลัง",power,"เท่ากับ",pow(listA[i], power) )
def myfunction1(mylistA):
    print("Hello, From function 3.")
    return mylistA
