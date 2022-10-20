"""
Name: Jirayut Jeebjong
ID: 364411760011
Group: MIT421
"""
print("Start")
def division(a,b):
    try:
        return a/b
    except:
        raise ZeroDivisionError("devide by zero")

try:
    rs = division(10,0)
    print("The result: ",rs)
except Exception as e:
    print("Error log: ",e.args)

print("End")