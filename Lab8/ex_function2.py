"""
Name: Jirayut Jeebjong
ID: 364411760011
Group: MIT421
"""

# function with multiple parameter

def myfunc(*msg): # *msg --> tuple (...)
    print(msg)
    print(type(msg))

def myfunc2(*value):
    total = 0
    for x in value:
        total += x
    #print(total)
    return total


myfunc(10)
myfunc(10,20,30)

x = myfunc2(10)
x = myfunc2(99,88,77,44,55)
print(x)