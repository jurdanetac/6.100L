# Finger Exercise Lecture 5
# Name: Juan Urdaneta
# Collaborators: None
# Time Spent: 0:05

# Assume you are given a string variable named my_str.
# Write a piece of Python code that prints out a new string containing the even indexed characters of my_str.
# For example, if my_str = "abcdefg" then your code should print out aceg.

even_str = ""
for i in range(my_str):
    if i % 2 == 0:
        even_str += my_str[i]
