#_________________________________
# File : 01_operator_basics.py
# Purpose : Learn operators in python
# Concepts : 
# - arithmetic operators
# - relational operators
# - assignment operators
# - logical operators
#___________________________________

# An operator is a symbol that performs a certain operation between operands.
# a + b 
# a and b are operands and + is operator

#Types of operators

# 1- aeithmetic operators

a = 10
b = 2

print(a + b) #addition
print(a - b) #subtraction
print(a * b) #multiplication
print(a / b) #division (answer is always in 'float' value)
print(a % b) #remainder
print( a ** b) #a^b

# 2- reational operators/ comparision operators
# answer will be always Trur or False

c = 50
d = 20

print(c == d) # the vale of (c) is equal to (d) or not
print(c != d) # the value of (c) is not equal to (d) or not
print(c > d)  # the vale of (c) is greater than (d) or not
print(c < b)  # the vale of (c) is smaller than (d) or not
print(c >= d) # the vale of (c) is greater than equal to(d) or not
print(c <= d) # the value of (c) is smaller than equal to (d) or not

# 3- assignment operators
# these are used to assign values to variables

num = 10
num = num + 10 #10+10 => 20
print("num :", num)

# other way to write this:
 
num1 = 10
num1 += 10 # 10+10 => 20
print("num1 :", num1)

num2 = 10

num2 -= 5 # 10-5 
print("num2 :", num2)

num2 *= 5 # 10*5 
print("num2 :", num2)

num2 /= 2 # 10/2 =< 
print("num2 :", num2)

num2 %= 5 # remainder
print("num2 :", num2)

num2 **= 2 # 10^2 

# 4- logical operators

# not operator
e = 50
f = 30
print(not(e>f)) #False
print(not(f>e)) # True

# and operator

# answer will be True if both the values are True
val1 = True
val2 = True
print("ans operator:", val1 and val2)

# if one of the value is False the answer will always be False
val3 = False
val4 = True
print("ans operator:", val3 and val4)

# or operator

# if one of the value is True the answer will be True
val5 = True
val6 = False
print("OR operator:", val5 or val6)

# answer will be False if both the values are False
val7 = False
val8 = False
print("OR operator:", val7 or val8)














