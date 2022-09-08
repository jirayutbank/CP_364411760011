"""
Name: Jirayut Jeebjong
ID: 364411760011
Group: MIT421
"""

# list
mylist = [10,20,30,40,50]
# add member to list
# append()
print(mylist)
# add 60 to my list
mylist.append(60)
print(mylist)

mylist2 = [100,200,300]

mylist.append(mylist2)
print(mylist)

mylist = mylist + mylist2
print(mylist)

# insert member to list
# insert(index,data)
mylist.insert(-3,400)
print(mylist)
# add 1000 to first number
mylist.insert(0,1000)
print(mylist)

# delete member to list
# remove()
mylist.remove(100)
print(mylist)

if 500 in mylist:
    print("list has no 500.")
else:
    print("list has no 500.")
print(mylist)

# pop
# del last number
mylist.pop()
print(mylist)
#del first number
mylist.pop(0)
print(mylist)

# del
# del first number
del mylist [0]
print(mylist)

#del mylist2
print(mylist2)

# change data in list
mylist[-1] = 2000
print(mylist)

mylist[0] = mylist[0]*100
print(mylist)

# sorting data in list
mylist2 = mylist

# sort()
mylist.sort() # low to high
print(mylist)

mylist.sort(reverse=True) # high to low
print(mylist)

# reversed()
print(mylist2)

# copy
newlist = mylist.copy()
mylist.append("MIT421")
print(mylist)

print(newlist)