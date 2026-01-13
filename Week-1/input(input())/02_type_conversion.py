#___________________________________
# File :02_type_convesion.py
# Purpose : Learn type conversion
# Concepts :
# - Type conversion
# - Type casting
# - Error
#____________________________________

# Learning type conversion

a = 2
b = 4.25

sum_reasult = a + b  # Python automatically convert 'int' value into 'float' value (2.0 +b4.25)
print(sum_reasult) # 6.25


# Learning type casting

e = 1.0
f = "2"
g = int(f) # in order to add 'float' and 'str' value, have to convert 'str' into 'int' value
 
sum_reasult = e + g
print(sum_reasult) # 1.0 + 2

# Error
c = "5"
d = 6.5

sum_reasult = c + d
print(sum_reasult) # can't add 'str' value with 'float' value automatically






