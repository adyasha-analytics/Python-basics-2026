#_________________________________
# File : 01_for_loops.py
# Purpose : Learning for loops
# Concepts :
# _ list
# - tuples
# - string
# - else
# - break
#____________________________________

#Loops : thse are used for sequential travels. For traversing list, string, tuples, etc.

#for loops

nums = [1, 2, 3] #list
for val in nums:
    print(val)

veggies = ["patato","brinjal","ladyginger","cucumber"] #list
for val1 in veggies:
    print(val1)

tup = (1,2,3,4,5,6,7,8,9) #tuples
for num in tup:
    print(num)

str = "Adyasha" #string
for char in str:
    print(char)

#elae (else runs only the loop finishes normally)

str1 = "Python"
for char1 in str1:
    print(char1)
else:
    print("END")   

#when the loop is stopped using break, else is SKIPPED

str2 = "code"
for char2 in str2:
    if(char2 == 'd'):
        print("o found")
        break
else:
    print("END")

