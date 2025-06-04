"""A – H, determine and explain the output displayed by the lines of code.  Save your code as PE4_6.py.  

A - F, using the given list, n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 

A 
print(n, n[:]) 
print(n[0], n[-10]) print(n[9], n[-1]) 
print(n[3:])         print(n[:5])         
print(n[-5:-1]) print(n[4:8]

B
print(n[-1] + n[-2]) 
print(n[9] - n[1]) 
print(n[2] * n[5]) print(n[8] / n[2]) 
print(len(n), n[:len(n)], sep = '\n') 
print(min(n), max(n), type(n), sep = '\t') 

C 
n[0], n[9] = "apple", 'cherry' n.insert(3, "banana") 
n.insert(-1, "kiwi") 
print(n) 
print(f"Do you like {n[0].upper()} or {n[-1].upper()}?") 

D 
n.append(-11)             
n.append("orange") 
n[0], n[1] = n[-1], n[-2] 
print(n+n) print(n*2) 

E 
item1 = n.pop(0) 
print(f"{item1} is removed.") 
item2 = n.pop() 
print(f"{item2} is removed.") 
print('n = ', n) 
print(f'Removed items: {item1} & {item2}') 

F 
n.insert(6, 'pear') 
del n[-1] del n[0] 
print(n) 
n.remove("pear") 
n.remove(6) 
print('n = ', n) 
n.clear() 
print(f'n = {n}') 

G 
fruits = ['kiwi', 'pear', 'orange', 'apple', 'cherry'] 
fruits.sort() print(fruits[0], fruits[-1]) 
fruits.sort(reverse=True) 
print(fruits[0], fruits[-1]) 

H 
fruits = ['kiwi', 'pear', 'orange', 'apple', 'cherry'] 
print(sorted(fruits)) print(fruits[0], fruits[-1])  
print(sorted(fruits, reverse=True)) 
print(fruits[0], fruits[-1]) 



"""


# A 
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(n, n[:]) 
# The line prints two interations of the n variable 

print(n[0], n[-10]) 
# The line prints the first index of variable n, which is 1. The second parameter will print print the first inex because theres no 10th index to start at.

print(n[9], n[-1]) 
# This line prints the nunber 10. the second arguement for the print function displays 10

print(n[3:])   
# This line prints from the 3rd index to the last index

print(n[:5])     
    # This line prints the first to 4th index which is number 1 -5 

print(n[-5:-1]) 
# This prints the 5th index from the end all the way to the end of the array which displays 6 - 9

print(n[4:8])
# This prints the 5th index to the 8th which displays 5-8


# B

"""A – H, determine and explain the output displayed by the lines of code.  Save your code as PE4_6.py.  

"""
print(n[-1] + n[-2]) 
# This line prints the last index in the list concatinated with 

print(n[9] - n[1]) 
# `print(n[9] - n[1])` subtracts the value at index 1 from the value at index 9 in the list `n`. 
# `n[9]` points to the element at index 9, which is `10` & `n[1]` corresponds to the element at index 1, which is `2`.
# Therefore, the output will be `10 - 2`, which equals `8`.

print(n[2] * n[5]) 
# `print(n[2] * n[5])` multiplies the value at index 2 with the value at index 5 in the list `n`.
# `n[2]` refers to the element at index 2, which is `3` & `n[5]` refers to the element at index 5, which is `6`.
# The output will be `3 * 6`, which equals `18`.

print(n[8] / n[2]) 
# the function `print(n[8] / n[2])` divides the value at index 2 by the value at index 8 in the list `n`.
# `n[8]` corresponds to the element at index 8, which is `9` & `n[2]` points to the element at index 2, which is `3`.
# The output will be `9 / 3`, which equals `3.0` (the result is a floating-point number).

print(len(n), n[:len(n)], sep = '\n') 
"""
In this function `print(len(n), n[:len(n)], sep='\n')`,`len(n)`vprints the length of the list `n`, which is the number of elements in the list. In this case, it's 10.
`n[:len(n)]`vprints the elements of the list from the beginning up to (but not including) the length of the list. Essentially, it prints the entire list.
`sep='\n'` sets the separator between the two printed values to a newline character, making each output appear on a new line.

"""
print(min(n), max(n), type(n), sep = '\t') 
# print(min(n), max(n), type(n), sep='\t')`:
# `min(n)` prints the minimum value in the list `n`, which is 1.
#`max(n)` prints the maximum value in the list `n`, which is 10.
#`type(n)` prints the type of the variable `n`, which is `<class 'list'>`.
#`sep='\t'` sets the separator between the printed values to a tab character.


# C
n[0], n[9] = "apple", 'cherry'
# assigns the value "apple" to the first element of the list (index 0) and 'cherry' to the last element of the list (index 9).
 
n.insert(3, "banana") 
#`n.insert(3, "banana")` inserts the value "banana" at index 3 of the list. So, the list becomes `[1, 2, 3, 'banana', 4, 5, 6, 7, 8, 'cherry']`.

n.insert(-1, "kiwi") 
# uses insert method to insert the value "kiwi" at the second-to-last position in the list (index -1)


print(n) 
# prints the list modified with the previous insert methods.
# the list becomes `['apple', 2, 3, 'banana', 4, 5, 6, 7,8, 'kiwi', 'cherry']`.

print(f"Do you like {n[0].upper()} or {n[-1].upper()}?") 
# `print(f"Do you like {n[0].upper()} or {n[-1].upper()}?")` prints a formatted string using f-string. 
# It prints a question asking if you like the uppercase version of the first element ('APPLE') or the last element ('CHERRY') & displays 'Do you like APPLE or CHERRY?'

print("------------------------------------------------------------------------")
# D
n.append(-11)       
# '-11' is added to the end of the list with the append method
 
n.append("orange") 
# This append method attaches the string 'orange' to the list 

n[0], n[1] = n[-1], n[-2] 
# This line of code brings the data from the last two indexes to the indexes '0' and '1'

print(n+n)
# this prints the updated list twice with the two new d=first indexes defined in the previous line of code. 

print(n*2) 
# this print function prints the lists twice, similarly to the previous line of code. 


print("------------------------------------------------------------------------")



#E
item1 = n.pop(0) 
# this line of code declares a variable 'item1' with the pop method attached to the n list. 

print(f"{item1} is removed.") 
# the print function is used with a format method to store the varables data into the string in the print function. The output will be the string in the print function with "orange" in place of 'item1'

item2 = n.pop() 
# this line decalres a pop method on th 'n' list in a new variable called 'item2' but nothing is take in as an arguement so there will be nothing popped into the list 

print(f"{item2} is removed.") 
# the print function is used with a format method to store the varables data into the string in the print function. The output will be the string in the print function with "orange" in place of 'item1'

print('n = ', n) 
# The print function displays the string "n: " with the list variable 'n' contents: "n =  [-11, 3, 'banana', 4, 5, 6, 7, 8, 9, 'kiwi', 'cherry', -11]"

print(f'Removed items: {item1} & {item2}')
# This line prints a string with the variables item1 and item2 formatted into it. "Removed items: orange & orange" is displayed

print("------------------------------------------------------------------------")


# #F
n.insert(6, 'pear') 
# This line inserts the string 'pear' into the 6th index giving a new list [-11, 3, 'banana', 4, 5, 6, 'pear', 7, 8, 9, 'kiwi', 'cherry', -11]


del n[-1] 
# index 10 from the list 'n' is deleted removing -11

del n[0] 
# this deletes the first index in the list; the int -11

print(n) 
# The updated list is printed [3, 'banana', 4, 5, 6, 'pear', 7, 8, 9, 'kiwi', 'cherry']

n.remove("pear") 
# this line finds the string "pear" and removes it

n.remove(6) 
# this line removes the first occurance of the number 6. The list is now [3, 'banana', 4, 5, 7, 8, 9, 'kiwi', 'cherry']

print('n = ', n) 
# This prints the list with the string 'n= ' and comma seperation 

n.clear() 
# This line clears the string

print(f'n = {n}')
# this line of code prints the cleared string with the format method and the n variable
print("------------------------------------------------------------------------")


# #G
fruits = ['kiwi', 'pear', 'orange', 'apple', 'cherry'] 
# This line of code declares a variable named fruit as a list of strings with many fruit in it.

fruits.sort() 
# The sort method being used on the fruits list sorts the fruit and displays them in alphabetical order ['apple', 'cherry', 'kiwi', 'orange','pear']

print(fruits[0], fruits[-1]) 
# The print function takes in two areguments, The first is the first index of the fruit list. The second is the last index from the fruit list. These are apple and pear.

fruits.sort(reverse=True) 
# The sort method is used on the fruits list but reversed is set to true as the arguement to the method, reversing the list.

print(fruits[0], fruits[-1])
# The print function prints the first and last index of the newley reversed list


print("------------------------------------------------------------------------")

# H

fruits = ['kiwi', 'pear', 'orange', 'apple', 'cherry'] 
# This line of code declares a variable named fruits as a list of strings with many fruit in it.


print(sorted(fruits)) 
# The print function takes in sorted() as a parameter and and hold the fruits list within that parameter. This returns the list sorted permanently as ['apple', 'cherry', 'kiwi', 'orange', 'pear']

print(fruits[0], fruits[-1]) 
# The print function takes in two areguments, The first is the first index of the fruit list. The second is the last index from the fruit list. However, these indexes data is taken from the original lists order.

print(sorted(fruits, reverse=True)) 
# The print function takes in sorted() as a parameter and and hold the fruits list within that sorted methods parameter with 'reverse=true'. This returns the list sorted permanently and reversed as ['pear', 'orange', 'kiwi', 'cherry', 'apple']

print(fruits[0], fruits[-1]) 
# This print fucntion return the first and the last index of the newly sorted and reversed fruits list. The terminal prints kiwi and cherry 
