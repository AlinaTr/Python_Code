#  Arithmetic operators
x = 2
y = 3

#  addition
print(x + y) # 5

#  substraction
print(x - y)

# multiplication
print(x * y) # 6

# division
print(y / x ) # 1.5

#   modulus
print(y % x ) # 1

# exponentiation
print(x ** y) # 2 la puterea 3 = 8

# floor division

# string multiplication
my_str = 'a'

# I want to display the message 'aaa'
print(my_str + my_str + my_str)
print(my_str *3 )

"""
1. Two variables are given, a = 10, b = 2.
 Perform all operations on the 2 variables,
using arithmetic operators.
"""
a = 10
b = 2
print(a + b) # 12
print(a - b) # 8
print(a * b) # 20
print(a / b) # 5.0
print(a % b) # 0
print(a // b) # 5
print(a ** b)  # 100

"""
2. 
a. Read a number from the keyboard
b. Check, using assert, if the read number is an even number.
"""
# number = int(input('Number: '))
# assert number % 2 == 0

# Floor division: // operator
# Round the result to the nearest integer
#  On what principle is rounding done?
#  The integer to which it is oriented must fulfill the following condition: Result <= the integer of the result.

x = 17
y = 2
print (x // y) # 8.5 -> rezultatul este 8

x = 2
y = 3
print(y // x) # 3 // 2; 1.5 => 1

# Assignment operators

# ASSIGNMENT OPERATORS
# 1. Solve the exercise from the ARITHMETIC OPERATORS section
# using ASSIGNMENT OPERATORS.

# # print(a + b) # 12
# # a += b
# print(a) # 12

# # print(a - b) # 8
# # a -= b
# print(a)

# # print(a * b) # 20
# # a *= b
# print(a)

# # print(a / b) # 5.0
# a /= b
# print(a)

# Logical operators

# 1. For each of the examples below, write in a comment
# the expected result, then uncomment the code from each example, in turn
# and run the examples and check the output.

#  Example 1:
# a = True
# b = False
# print(not(a)) # False
# # print(not(b)) # True
#
# # Example 2:
# # a = True
# # b = False
# # x = not(a) # False
# # y = not(b) # True
# # print(a or b) # True or False -> True
# # print(x or y) # False or True -> True
# # print(a or x) # True or False -> True
# # print(x or b) # False or False -> False

# # Example 3:
# a = False
# b = False
# x = not(a) # True
# y = not(b) # True
# print(a and b) # False and False -> False
# print(a and x) # False and True -> False
# print(y and b) # True and False -> False
# print(x and y) # True and True -> True

# COMPARISON OPERATORS

# 1.
#  a. The variable num = 12 is given
num = 12
# b. Using assert, check if the number read is positive.
assert num >= 0
# c. Using assert, check if num is greater than 5.
assert num > 5
# d. Using assert, check if num is less than 25.
assert num < 25
# e. Using assert, check if num is between 0 and 20
assert num >0 and num < 20
assert 0 < num < 20