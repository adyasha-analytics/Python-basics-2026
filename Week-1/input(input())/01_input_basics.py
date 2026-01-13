#______________________________
#File : 01_input_basic.py
#Purpose : Learn python input()
#Concepts :
# - input()
# - print()
# - Reasult of input
# - Type casting
#_______________________________

# input() statement is used to accept values (using keybord) from users

input("enter your name:")

# Printing input() values

age = input("enter your age:")
print("my age is:", age)

# Reasults for input() is always a str

val = input("enter some value:") # value: Megha
print(type(val), val) # 'str'> megha

val1 = input("inter some value:") # value: 25
print(type(val1), val1) # 'str'> 25

# Type casting for integer value
# Code format: int(input()) 

val2 = int(input("enter some value:")) # value: 99
print(type(val2), val2) # 'int'> 99

# Type casting for floating value
# Code format: float(input()) 

val3 = float(input("enter some value:")) # value: 35
print(type(val3), val3) #'float'> 35.0

# Assignment

name = input("enter your name:") # Adyasha
age = input("enter your age:") # 18
marks = input("enter your marks:") # 98.99

print("name:", name) # name: Adyasha
print("age:",age) # age: 18
print("marks=",marks) # marks= 98.99
