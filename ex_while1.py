"""
Name: jirayut Jeebjong
Id: 364411760011
Group: MIT421
"""

# while loop

# รับค่าจากผู้ใช้ไปเรื่อยๆ แต่หากผู้ใช้ใส่ค่าเลข 0 ให้หยุดการทำงานของลูป
i = 0
while i < 10:
    num = int(input("Enter an integer"))
    print("your number is : ",num)
    if num ==0:
        print("good bye.")
        continue
    i += 1