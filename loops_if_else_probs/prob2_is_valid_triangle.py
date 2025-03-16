# Problem 2: Write a program that take a user input of three angles and will find out whether it can form a triangle or not.


## Initial versio:
 #ask 2 angles to enter form user
angle1 = float(input("enter angle1: "))
angle2 = float(input("enter angle2: "))
angle3 = float(input("enter angle3: "))

 # sum of angles in triangle
sum_of_triangles = angle1 + angle2 + angle3

if sum_of_triangles == 180:
    print("the angles form triangle")
else:
    print("angles are not forming triangle")    


#------------------------------------------
#optimized version:

def is_valid_triangle(angle1, angle2, angle3):
    """check if angle can form a valid triangle"""
    if any(angle <= 0 or angle >= 180 for angle in (angle1,angle2,angle3)):
        return "Invalid input! Angles must be between 1 and 179 degrees."
     
    return "The angles form a triangle" if(angle1 + angle2 + angle3) ==180 else "Angles do not form a triangle."
    
 #get user input safely
try:
    angle1 = float(input("Enter angle 1: ").strip())  
    angle2 = float(input("Enter angle 2: ").strip())
    angle3 = float(input("Enter angle 3: ").strip())

    print(is_valid_triangle(angle1, angle2,angle3))
except ValueError:
       print("Invalid input! Please enter numerical values.")


# The .strip() method is used to remove any leading or trailing whitespace from the user input before converting it into a float.
# ##🔹 Error Handling in Python
# Error handling in Python is done using the try-except block. It allows a program to catch and handle errors gracefully instead of crashing.

# 1️⃣ Basic Syntax

# try:
#     # Code that may cause an error
#     result = 10 / 0  # Division by zero error
# except ZeroDivisionError:
#     # Handle the error
#     print("Cannot divide by zero!")

# ##🔹 How it works?

  # The try block runs the code that might cause an error.
  # If an error occurs, the except block catches and handles it.