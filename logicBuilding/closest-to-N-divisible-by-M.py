"""
Given two integers n and m (m != 0). Find the number closest to n and divisible by m. If there is more than one such number, then output the one having maximum absolute value.

Examples: 

Input: n = 13, m = 4
Output: 12
Explanation: 12 is the closest to 13, divisible by 4.

Input: n = -15, m = 6
Output: -18
Explanation: Both -12 and -18 are closest to -15, but -18 has the maximum absolute value.
"""

# # The basic idea is to start checking from n - m to n + m one by one and take the closest number.
# def closestNumber(num, div):
#   closest = 0
#   min_dif = float('inf')
#   for i in range(num - abs(div), num + abs(div) + 1):
#     if (i % div == 0):
#       dif = abs(num - i)
#       if (dif < min_dif) or (dif == min_dif and abs(i) > abs(closest)):
#         closest = i
#         min_dif = dif
#   print(closest)

# number = int(input("Enter Number: "))
# divisor = int(input("Enter Divisor: "))
# closestNumber(number, divisor)


"""
We first compute the quotient q = n / m, then calculate two candidates:

1. n1 = m * q
  This is the closest multiple of m that is less than or equal to n.
2. n2 = m * (q + 1) or m * (q - 1)
  We choose q + 1 or q - 1 based on the signs of n and m:
    i.  If n and m have the same sign, use n2 = m * (q + 1)
        This moves in the direction toward n, getting the next closest multiple above n.
    ii. If n and m have opposite signs, use n2 = m * (q - 1)
        This accounts for the fact that increasing q would move away from n due to the sign flip, so we instead go backward to get the next closest multiple.
  Then we return the one (n1 or n2) that has the smaller absolute difference from n.

If both have the same distance from n, return the one with the greater absolute value, as required.
"""

def closestNum(number, divisor):
  quotient = int(number/ divisor)
  n1 = quotient * divisor
  if (number * divisor > 0):
    n2 = divisor * (quotient + 1)
  if (number * divisor < 0):
    n2 = divisor * (quotient - 1)
  
  if (abs(number - n1) < abs(number - n2)):
    return n1
  else: 
    return n2
  
num = int(input("Enter a Number: "))
div = int(input("Enter Divisor: "))
print(closestNum(num, div))