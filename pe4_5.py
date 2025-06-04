
"""
Requests a name from the user. Save the code as PE4_5.py.  

a)   Use Input() to prompt and request a full name.    
b)   After the user types the full name and presses the Enter (or Return) key,   display the first name and last name in two separate lines.  

Input text can be any content.  Just make sure to precisely match the output format below.    
Example Output 1:  
Enter the full name of your favorite US president:  george washington  
First Name: George  
Last Name: Washington 

Example Output 2:  
Enter the full name of your favorite US president:  Franklin Delano Roosevelt  
First Name: Franklin 
 Last Name: Roosevelt 

"""

fullname = input("Enter names: ")
names = fullname.split(' ')
firstname = names[0]
lastname = names[-1]

print(firstname)
print(lastname)

