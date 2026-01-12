# ============================================
# File: 05_lecture_practice.py
# Purpose: Practice of Week-1 Python concepts
# ============================================

# ---------- VARIABLES ----------
# Variables are used to store data in memory

name = "Adyasha"     # string type variable
age = 18             # integer type variable

# ---------- PRINT FUNCTION ----------
# print() is used to display output on the screen

print("My name is", name)
print("My age is", age)

# ---------- ARITHMETIC OPERATIONS ----------
# Performing basic mathematical operations using variables

a = 23
b = 35

sum_result = a + b          # addition
difference = b - a          # subtraction

print("Sum:", sum_result)
print("Difference:", difference)

# ---------- DATA TYPES ----------
# type() is used to check the data type of a variable

print("Type of name:", type(name))          # <class 'str'>
print("Type of age:", type(age))            # <class 'int'>
print("Type of sum_result:", type(sum_result))  # <class 'int'>

# ---------- BOOLEAN & NONE (EXTRA PRACTICE) ----------
# Boolean stores True or False
# None represents absence of value

is_student = True
result = None

print("Type of is_student:", type(is_student))
print("Type of result:", type(result))
