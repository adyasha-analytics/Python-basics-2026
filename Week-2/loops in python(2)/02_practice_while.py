#_________________________________
# File : 02_practice_while.py
# Purpose : practice while loop
# Concept: 
# - print numbers
# - multiplaction
# - list
# - tuple
# - search for number
#__________________________________

#print numbers from 1 to 100

a = 1 #starting condition
while a <= 100: #stoping condition
    print(a)
    a += 1

#print numbers from 100 to 1

b = 100 #starting condition
while b >= 1: #stoping condition
    print(b)
    b -= 1

#print multiplaction table of number n

n = int(input("enter number :"))
c = 1
while c <= 10:
    print(n*c)
    c += 1

#traverse

#print the elements of the following list using a loop [1,4,9,16,25,36,49,64,81,100]

nums = [1,4,9,16,25,36,49,64,81,100]

idx = 0
while idx < len(nums):
    print(nums[idx]) #nums[0], nums[1], nums[2]
    idx += 1

#search for a number x in this tuple using loop:(1,4,9,16,25,36,49,64,81,100)

nums1 = (1,4,9,16,25,36,49,64,81,100)

x = 36

d = 0 #initilazation
while d < len(nums1):
    if(nums[d] == x):
        print("FOUND at idx", d)
    d += 1