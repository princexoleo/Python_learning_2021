"""
Created by Mazharul Islam Leon

"""




"""
 This is for basics Python Code.
 You can learn the basic syntax & structure of Python
 How to print in Python ?
 How Debug in Python ?
 How to Identify Error Message ?
 How to Initialize the different types variable ?
 How to declare String in Python ?
 Lot more things ... Lets start
"""

# this symbol use in Python for comment line

# -----------------                                -------------------- #
#                         Day - 1 Learning 

# -----------------                                -------------------- #



print("Hello World")

# double quotation means the starting and ending of a String 
# Parenthesis is the syntax of Python. if it is missing then It will show
# the SyntaxError: unexpected EOF while parsing.
# Also if you miss to insert double quotation, then it also show the #SyntaxError
# The error message can be shows in the shell/output terminal.

# More example of Parenthesis and String Manipulation are given below:
print("Day 1 - String Manipulation") # Inside double quotation you can use space, symbol etc.
# if you want to print double quotation in a String, then you have to use Nested quotation
print('String Concatenation is done with the "+" sign.') 
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")
# expample print("\n")
# Now if you want to use Nested print options:
print(print("Here is nested print"))

# if you want to print Same line into 3 times then
# we use:
"""
 print("Line 1")
 print("Line 2")
 print("Line 3")

 but there is another option available. Like:
 print("Line 1\nLine 2\nLine 3")
 The line are seperated by \n 

"""
print("Line 1\nLine 2\nLine 3")

# Combine 2 string :
"""
 string 1: Hello
 sting  2: Leo

 solution 1 : print("Hello "+"Leo")
 solution 2 : print("Hello" + " " + "Leo")

We combine two string by using "+" sign in between two string.
"""
print("Hello "+"Leo")
print("Hello" + " " + "Leo")

# In python programming Spaces are very important, So we need to 
# be becareful when we use space 
"""
print("something")
    print("Something") # we use tab space before this line

When we execute the program then this will shows a Error.
The error message is like: IndentationError: Unexpeced indent

Python is more sensitive to indent error.
Paying attention when we typing code can be a solution.
Text editor also a solution/ can be helpful. Most of the IDE can have features to 
help in this problem. 
"""

# -----------------------Excercise-1 Problem---------------------
"""
Try to identified the error and solve it by yourself.
If you look at this error and find out the reason, then definetly it this
learning will help you in future. You can easily identify the error & Save your time.
Fix the code below:

print(Day -1 String Manipulation")
print("String Concatenation is done with the "+" sign.")
    print('e.g. print("Hello " + "world")')
print(("New lines can be created with a backlash and n."))

"""

#--------------------------Solution of Excercise-1 --------------------
print("Day -1 String Manupulation")
print("String Concatenation is done with the '+' sign.")
print('e.g. print("Hello "+"world")')
print(("New lines can be created with a backlash and n."))
