# for ใช้กรณีซ้ำมีจำนวนรอบ
for i in ["1,2,3,4,5"]: #เรียงลำดับจากข้อมูล
    print(i)

for i in range(101): #เรียงลำดับอัตโนมัติ
    print(i)

#ทำซ้ำข้อมูลไปเรื่อยๆ ตราบใดที่เงื่อนไขข้อมูลยังจริงอยู่ --> while loop
x = 100
while x>0:
    print(x)
    x = x-1
# infinite loop ทำซ้ำจนกว่าจะใส่ข้อมูลถูกต้อง
while True:
    name = input("Enter your name: ")
    if name == "bank":
        print("สวัสดีครับ " +name)
        break
    print("พิมพ์ชื่อจนกว่าจะถูก " + name)

# function
def greet(name):
    print("Hello "+name)
greet("bank")
greet("bann")
greet("boom")

def yok3(x): #เลกยกกำลัง
    return x**3

a = yok3(2)
print(a)

