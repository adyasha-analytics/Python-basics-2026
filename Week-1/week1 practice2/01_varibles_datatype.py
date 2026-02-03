#____________________________________________________________________________________________________________
#File: 01_varibles_datatype.py
#Purpose: Practice
#concept:
# - variables
# - data type
# - Re-assignment
#___________________________________________________________________________________________________________

a = 5
b = 5.0
c = "5"

print(type(a)) #int
print(type(b)) #float
print(type(c)) #str

x = "10"
y = 10

print(x + x) # "1010" (for str '+' means conection)
print(y + y) #20 

#for numeric addition

v = "10"
v = int(v)

print(v + v) #20

#Re-assignment

d = 10
e = d
d = 5

print(d) #5
print(e) #10 (e still points the old value)

f = 5 
g = f
f = f + 1

print(f) #6
print(g) #5 

#trap question

h = "5"
h = h + "1"

print(h) #"51"