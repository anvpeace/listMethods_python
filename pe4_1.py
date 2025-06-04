"""
A – C, determine the output displayed by the lines of code.
"""

# Question 1 Part A

print("Python") 
# This line will display the whole string 'python'

print("Python"[0]) 
# This will display the first letter which is placed at index 0, "P"

print("Python"[-1]) 
# This print function will display "n" the last letter of the string "Pyhton"

print("Python"[:]) 
# The whole string "Python" will be output


# ======================================================================

# Question 1 Part B

str = "Python 123" 
print(str) 
# The variable string will be printed 

print(str[0])
# The letter at index 0 will be printed "P" 

print(str[-1]) 
# The last letter of the str variable will be printed; "3"

print(str[:]) 
# The whole string variable will be printed


# ======================================================================

# Question 1 Part C

strNum = "0, 1, 2, 3, 4, 5, 6, 7, 8, 9" 
# A string variable with a list of numbers is declared.

print(strNum[1], strNum[-1], len(strNum)) 
# With comma seperation this line prints out the second index in the string ",", the last index in the string "9", and the length of the string "28" is returned with last argument in print command

print(strNum[:len(strNum)]) 
# The entire strNum will be printed 

print(strNum[1]+strNum[-3])
# This will return "," and "," as both commas are placed in the second and second to last index