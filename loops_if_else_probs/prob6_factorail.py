# Problem 6 - Find the factorial of a given number.
# Write a program to use the loop to find the factorial of a given number.

# The factorial (symbol: !) means to multiply all whole numbers from the chosen number down to 1.


# version 1-Using while Loop
def factorial(n):
    result =1
    while n>1:
        result *= n
        n = n-1
    return result

n = int(input("Enter a number: "))
print(f"Factorial of {n} = {factorial(n)}")


################################################################
# version 2-Recursive Factorial 
def factorial(n):
   if n==1 or n==0:
    return 1
   return n*factorial(n-1) 


n = int(input("Enter a number: "))
print(f"Factorial of {n} = {factorial(n)}")


##################################################################
#version 3-math.factorial()
import math 

n = int(input("Enter a number: "))
print(f"factorial of {n} = {math.factorial(n)}")
