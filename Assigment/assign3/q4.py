"""
Name: Jirayut Jeebjong
ID: 364411760011
Group: MIT421
"""

#4. เขียนฟังก์ชันเพื่อค่าหาต่ าสุด และค่าสูงสุด ให้ return ผลลัพท์ทั้ง 2 ออกมา ก าหนดให้ฟังก์ชันนี่รับparameter 1 ตัว คือ listA ที่มีสมาชิกเป็นจ านวนใดๆ
a = int(input("function1 : "))
b = int(input("function2 : "))
c = int(input("function3 : "))
d = int(input("function3 : "))
listA = [a,b,c,d]
print(listA)
print("ค่าต่ำสุด คือ ",min(listA))
print("ค่าสูงสุด คือ ", max(listA))
def myfunc(listA):
    listA = [a, b, c, d]
    print(listA)
    print("ค่าต่ำสุด คือ ", min(listA))
    print("ค่าสูงสุด คือ ", max(listA))
    return (listA)
