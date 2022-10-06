"""
Name: Jirayut Jeebjong
ID: 364411760011
Group: MIT421
"""

# Function
# 1. Build-in function
print("Hello, MIT421")
s = "RUTS"
print(len(s))

# 2. create by owner -- using "def" keyword

def myfunction1():
    print("Hello, From function 1.")

def myfunction2(msg):
    print("Hello, From function 2.",msg)

def myfunction3(num1,num2):
    print("Hello, From function 3.")
    return num1+num2

# calling function
myfunction1()

# calling function with parameter
myfunction2("RUTS")

#calling function with parameter and return statement
rs = myfunction3(10,10)
print(rs)

print(myfunction3(20,20))
