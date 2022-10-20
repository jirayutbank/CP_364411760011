"""
Name: Jirayut Jeebjong
ID: 364411760011
Group: MIT421
"""

# Exeption
print("Start")
while True:
    try:
        num = int(input("Enter and integer: "))
        print(f'Your number is {num}')
        break
    except ValueError as e:
        print("Error log: ",e.argsa)
        print("Please, enter only integer.")

print("End")