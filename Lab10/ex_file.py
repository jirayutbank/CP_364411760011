"""
Name: Jirayut Jeebjong
ID: 364411760011
Group: MIT421
"""

# File I/0

# open file

f = open("test.txt")
print(f.read()) # read all text in a file
f.close()

f = open("test.txt")
print(f.read(10)) # read 10 charecters form file
f.close()

f = open("test.txt","r")
print(f.readline())
print(f.readline())
f.close()

f = open("test.txt")
line = f.readlines() # read line to list
for x in line:
    print()
f.close()

print(line)

count = 1
for x in range(len(line)):
    print(count,line[x])
    count += 1
    if count ==3:
        break
    count += 1

