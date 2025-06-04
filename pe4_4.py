# a)   Create an empty list named grades.  
grades = []

# b)   Add any five grades one at a time to grades. 
grades.insert(0, float(99.9))
grades.insert(1, float(96.2))
grades.insert(2, float(58.1))
grades.insert(3, float(93.7))
grades.insert(4, float(56.2))



# c)   Print the current list.  
print("Current List: ", grades)

# d)   Compute the total of these grades using the indexing to reference each number in grades. 

sum = grades[0] + grades[1] + grades[2]

# e)   Compute the average of these grades using the len () function. 
average = (sum / len(grades))

#  f)    Print the average with a precision of two decimal places.  
print("Average: ", '%.2f' %average)

# g)   Use two different methods to remove all failing grades (lower than 60) one at a time from the list. 

for grade in grades:

    if grade <= float(60.0):

        grades.remove(grade)







# h)   Print the updated list. 
print(grades)



