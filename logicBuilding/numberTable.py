# ------------ DAY- 1 -----------
# Given Number is n, print table of it.
'''
# using for loop:
def numberTable(n): # creating function
  for i in range(1, 11, 1):
    print("%d * %d = %d"%(n , i , (n*i)))

number = int(input("Enter a Number: "))
numberTable(number)

'''

# Using Recusive Function:
def numberTable(n, i =1):
  if (i == 11):
    return
  else:
    print(f"{n} * {i} = {n * i}")
    i += 1
  numberTable(n , i)


number = int(input("Enter a Number: "))
numberTable(number)