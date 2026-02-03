#____________________________________________________________________________________________________________
#File: 02_input_typeconversion.py
#Purpose: Practice
#Concept: 
# - input()
# - print
# - type conversion
#_____________________________________________________________________________________________________________

#without type conversion

x = input("enter a number:") 

print(x + x) #1010 (input() always runs a string)

#with type conversion

y = int(input("enter some number:"))

print(y + y) #20

#type check

a = input("enter first number:")
print(type(a)) #str

b = int(input("enter second number:"))
print(type(b)) #int

num = input("enter number:")
print(num * 2) #55 

num1 = int(input("enter number:"))
print(num1 * 2) #10