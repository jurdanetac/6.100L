# find cube root of positive cubes within some epsilon

cube = 27
epsilon = 0.01
low = 0
high = cube
guess = (low + high) // 2

# low---epsilon-guess-epsilon---high

while abs(guess**3 - cube) >= epsilon:
    if guess**3 > cube:
        high = guess
    elif guess**3 < cube:
        low = guess
    
    new_guess = (low + high) // 2
    guess = new_guess
    
print(guess)
