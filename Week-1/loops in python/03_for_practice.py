#_______________________________________
# File : 02_for_practice.py
# Purpose : Question practice
# Concepts :
# - print element
# - find X 
#________________________________________

# Print the elements of the following list using a loop: [1,4,9,16,25,36,49,64,81,100]

nums = [1,4,9,16,25,36,49,64,81,100]
for val in nums:
    print(val)

# Search for a number X in this tuple using loop: (1,4,9,16,25,36,49,64,81,100)

nums1 = [1,4,9,16,25,36,49,64,81,100]
X = 64

idx = 0
for val1 in nums1:
    if(val1 == X):
        print("number found at idx", idx)
    idx += 1

# print numbers from 1 to 100

for el in range(1, 101): #range (stop, start condition)
    print(el)

# print numbers from 100 to 1

for el1 in range(100, 0, -1): #range (stop, start, step)
    print(el1)

# print the multiplication table of a number n

n = int(input("rnter number :"))

for el2 in range(1,11):
    print(n * el2)

# write a program to find the factorial of first n numbers. (using for)
 
n1 = 5
fact = 1

for el3 in range(1, n1+1):
    fact *= el3

    print("factorial =el3", fact)
