"""
Task(1.1): Write a function named square that takes an integer n as input. It then prints the square of n. Use this function to print the square of 13.
"""
"""
Task(1.2): Use square function from Task 1.1 to print square of 11, 17 and 23.
"""

def squares(n):
  return n*n

num = int(input("Enter number to calculate square: "))
print(squares(num))
