# -*- coding: utf-8 -*-

# TP2 Data Types and `if` Structure

"""
Original file is located at
    https://colab.research.google.com/drive/1UbrFwL_jOAu_HVXvM_SxctZUBptFmM2f
"""


# Exercise 1 - Even or odd numbers? 
#Ask the user to enter a number then display whether it is even or odd?

#1. TODO
x = input("Please enter a number:")
x = int(x)
y = x%2
if y == 1:
	print("This is an odd number.")
else:
	print("This is an even number")


    
"""Exercise 2 - Ticket price
The price for visting a castle is as following:
+  free for children between 0 and 11 years old
+  5 euros for children between 12 and 17 years old and for adults over 60
+  10 euros for adults (18-59)

Write  a  program  that  asks  for  the  user’s  age  and  returns  the  price  charged.
"""

#2. TODO
x = input("Please enter your age:")
x = int(x)
if x < 12:
	print ("Price : 0")
elif 12 <= x < 18 or x >= 60:
	print ("Price: 5")
else:
	print ("Price : 10")
    


"""text{Exercise 3 - How much to pay employees? 
Write a program to ask the user for hours and rate per hour to compute gross pay, give the employee **1.5 times** the hourly rate for hours worked above **40 hours**.
"""

#3. TODO
x = input ("How many hours do you work?")
x = int(x)
y = input ("How much are you paid per hour?")
y = int(y)
z = x * y
if x > 40:
	print (z * 1.5)
else:
	print (z)



"""Exercise 4 - Which type?
Write a program to check the type of input that the user entered from the keyboard. 
Hints:
- `input()` function gets the user's input(which can be `str`,`int`,`float`... data) and returns always a string object. 
-  You can use `str()`,`int()` and `float()`functions in this exercice 
"""

#TODO
user_input = input("Enter something: ")
try:
	val = int(user_input)
	print("This is an integer.")	
except ValueError:
	try:
		val = float(user_input)
		print("This is a floating number.")
	except ValueError:
		print ("This is a string of characters.")



"""Exercise 5 - Handle Non-numeric Input
Rewrite your pay program of exercise 3 so that your program handles non-numeric input.
"""

#TODO
x = input("Please enter your age:")
try:
	x = int(x)
	if x < 12:
		print ("Price : 0")
	elif x == int and 12 <= x < 18 or x >= 60:
		print ("Price: 5")
	else:
		print ("Price : 10")	
except ValueError:
	x = input ("Please enter a number: ")
	try:
		x = int(x)
		if x < 12:
			print ("Price : 0")
		elif x == int and 12 <= x < 18 or x >= 60:
			print ("Price: 5")
		else:
			print ("Price : 10")	
	except ValueError:
		print ("You need to write down a number.")

### Je n'ai pas réussi à créer une boucle...







