"""
Given two numbers a and b, the task is to swap them.

Examples:

Input: a = 2, b = 3
Output: a = 3, b = 2

Input: a = 20, b = 0
Output: a = 0, b = 20

Input: a = 10, b = 10
Output: a = 10, b = 10 
"""

# 1. Using Third Variable (Naive approach):
num1 = 5
num2 = 6
temp = 0
print("a = ",num1 , "b = ", num2)
# Swapping
temp = num1
num1 = num2
num2 = temp
print("a = ",num1 , "b = ", num2)

# 2. Using Arithematic Operation:
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2
print("a = ",num1 , "b = ", num2)

# 3. Using XOR Bitwise Operator:
num1 = num1 ^ num2
num2 = num1 ^ num2
num1 = num1 ^ num2
print("a = ",num1 , "b = ", num2)

# 4. Using Tuple Unpacking In-Built feature:
num1, num2 = num2, num1
print("a = ",num1 , "b = ", num2)