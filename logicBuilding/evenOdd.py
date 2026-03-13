# ------------ DAY- 1 -----------
# Check given number n, is even or odd:

#Using Arithematic operation, if rem = 1 then, number is odd, rem = 0 then, number is even.

'''
def isEven(n):
  if (n % 2 == 0):
    return True
  else:
    return False

number = int(input("Enter a Number to check Even or Odd: "))
if (isEven(number)):
  print("Even")
else:
  print("Odd")

'''

# Using Bitwise Operator:

def isOdd(n):
  #Check Whether number is even or odd:
  if (n & 1) == 1:
    return True # if True Odd
  else:
    return False # if False Even

# Take Inputs
number = int(input("Enter a Number to check Even or Odd: "))

# Check Function is True or False:
if isOdd(number):
  print("Odd")
else:
  print("Even")