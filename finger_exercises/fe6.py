# Finger Exercise Lecture 6
# Name: Juan Urdaneta
# Collaborators: None
# Time Spent: 0:20

# Assume you are given an integer 0 <= N <=1000.
# Write a piece of Python code that uses bisection search to guess N.
# The code prints two lines:
# count: with how many guesses it took to find N, and
# answer: with the value of N.
# Hints: If the halfway value is exactly in between two integers, choose the smaller one.

interval = range(0, 1001)

count = 0
guess = 0

while guess != N:
    count += 1
    index = len(interval) // 2
    guess = interval[index]

    if guess == N:
        break
    elif guess < N:
        interval = interval[index:]
    else:
        interval = interval[:index]
        
print(f"count: {count}")
print(f"answer: {guess}")
