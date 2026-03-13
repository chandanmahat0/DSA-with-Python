# ------------ DAY- 2 -----------
"""
Given a positive integer n, we have to find the sum of squares of first n natural numbers. 
Examples : 

Input : n = 2
Output: 5
Explanation: 1^2+2^2 = 5

Input : n = 8
Output: 204
Explanation :  1^2 + 2^2 + 3^2 + 4^2 + 5^2 + 6^2 + 7^2 + 8^2 = 204 
"""

# Using loop:
def sumSquare(n):
  s = 0
  for i in range(1, n+1):
    s += i ** 2
  print("Sum of Square of first N natural number: ", s)

number = int(input("Enter number of first Natural Number: "))
sumSquare(number)

# 2. Using Mathematics Formula:
def sumSquare(n):
  s = (n * (n + 1)// 2) * (2 * n + 1)//3;
  print("Sum of Square of first N natural number: ", s)

number = int(input("Enter number of first Natural Number: "))
sumSquare(number)