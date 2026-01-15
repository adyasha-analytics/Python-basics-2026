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

