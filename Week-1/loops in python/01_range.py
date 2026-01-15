#_________________________________
# File : 01_range.py
# Purpose : Learn range in loop
# Concepts :
# - Basic of range function
# - sequence
# - loop in sequence
# - Ways to write range function

#__________________________________

#Range function returns a sequence of numbes, starting from 0 (by default), and increments by 1 (by default), and stops before a specified number.

print(range(5)) # range(0, 5)

seq = range(6)
print(seq[0]) #0
print(seq[1]) #1
print(seq[2]) #2
print(seq[3]) #3
print(seq[4]) #4

seq1 = range(10)

for el in seq1:
    print(el) 
    
    #or

for el1 in range(10):
    print(el1)

# (start?,stop,step?)

for el2 in range(9): #range(stop condition)
    print(el2)

for el3 in range(2, 9): #range(stop, start condition)
    print(el3)

for el4 in range(2, 9, 3): #range(stop, start, step condition)
    print(el4)
