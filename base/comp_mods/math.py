import time
print("Math Opening...")
time.sleep(8)
def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    return x / y
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
mtype = int(input("\n"))
in1 = float(input("number 1: "))
in2 = float(input("number 2: "))
if(mtype == 1):
    print(add(in1, in2))
if(mtype == 2):
    print(subtract(in1, in2))
if(mtype == 3):
    print(multiply(in1, in2))
if(mtype == 4):
    print(divide(in1, in2))