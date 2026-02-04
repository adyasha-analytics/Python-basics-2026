#____________________________________________________________________________________________________________
#File: 01_practice.py
#Purpose: revision
#Concept:
# - input
# - 0perators
# - if/eles
# - while loop basics
#______________________________________________________________________________________________________________

a = "10"
b = 10
c = "2"
d = 2

print(a + a) #1010
print(a * d) #1010
print(b * c) #2222...
print(b / d ) #5.0
print(b // d) #5
print(b % d) #0

x = "3"
y = 3
print(x == y) #False (the data type of x and y are different)
print(int(x) == y) #True (the data of x and y are same int.)

i = 5 #starting point
while i > 0: #condition
    print(i)
    i -= 2 #update

#Error (input alwars runs a string,even if you type numbers)

# num = input("enter a number:") 
# if num > 10:
#   print("big")
# else:
#    print("small")

#correct 

num = int(input("enter a number:")) 
if num > 10:
  print("big")
else:
    print("small")

#Print numbers from 10 to 0:

j = 10 #starting point
while j > -1: #condition
   print(j)
   j -= 1 #update

#check if number is divisible by 3:

num1 = 15
if num1 % 3 == 0: #remainder
   print(num1, "is divisible by 3")
else:
   print(num1,"is not divisible by 3")

#take input until user entrts 0:

num2 = int(input("enter some number:")) #starting point
while num2 != 0: #condition
   print("you entered:", num2)
num2 = int(input("enter some number:")) #update
print("loop ended")
