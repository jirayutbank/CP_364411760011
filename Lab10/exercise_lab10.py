"""
Name: Jirayut Jeebjong
ID: 364411760011
Group: MIT421
"""

"ให้นักศึกษาเขียนตารางสูตรคูณลงในไฟล์ test3.txt โดยการรับ Input แม่สูตรคูณ"

num = int(input("Enter your integer: "))

try:
    f = open("C:\\Users\LabCom_MT-4\Desktop\\test3.txt","a")
    for x in range(1,13):
        f.write(f'{num} x {x} = {num*x}\n')
except:
    print("Clound not found a file.")
finally:
    f.close()
    print("Done")