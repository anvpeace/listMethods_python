#a) Create an empty list called n.
n = []

#b Add 2 and 4 into the list. use append method
n.extend([2,4])

#d)Add 0, 1 and 3 in proper order.
# This block of code inserts numbers 0, 1, and 3, into indexes 0, 1, and 3. Then the new list is printed.
n.insert(0, 0)
n.insert(1, 1)
n.insert(3, 3)
print(n)

#f) Add 5 in proper order.
n.insert(5, 5)
print(n)

#h) Remove 0 from the list.
# The remove method on the n list with 0 as the parameter removes the number '0' from the list
n.remove(0)

#i print the list
print(n)

#j Remove and print 2 from the list.
one = n.pop(1)
# the pop method removes the data in index 1

# print(n)

print(one)

#l Remove and print 4 from the list.
four = n.pop(2)

print(four)

print(n)

#n) Add all the removed numbers and print the sum.
sum = one + four

print(sum)

#o) Change the first item to 100 and last item to 9.9.
n.insert(0, 100)

print(n)

n.append(9.9)

print(n)

#p Copy the list n to a newNum list.
newNum = list(n)

#q) Clear the list n.
n.clear()

#r) Print the original list, n and the newNum list.
print(n, newNum)

#s) Delete the list n.
del n

print(n)

