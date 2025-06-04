"""
A – C, identify the errors and rewrite the statements in the correct syntax.  Save your code as PE4_7.py
"""
# A
# Error:
# The index 3 does not exist
# myList = ['apple','banana','cherry'] 
# print(myList[3]) 

# Correct code
myList = ['apple','banana','cherry'] 
print(myList[2]) 


# B
# Error:
# index 4 does not exist to splice however an empty bracket is just returned. No error is thrown.
print(myList[-1:-4]) 

# C
# Error: 
# The string 'p' object being the list index is not supported with the variable assignment
# word = 'sea' 
# word[0] = 'p' 
# print(word) 

# Correct code:
word = 'sea' 
words = 'p'+ word
print(words) 



# D
# Error: 
# The items in the list cannot be joined as they are not all the same type of data 
# n = [1, "two", 'three', 4] 
# print(" ".join(n)) 

# Correct code:
n = ["one", "two", 'three', "four"] 
print(" ".join(n)) 