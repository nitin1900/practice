#my code woth many mistake but chatgpt solve and copy paste it...

import math
x = float(input("Enter x-coordinate: "))
y = float(input("Enter y-coordinate: "))
r = math.sqrt(x**2 + y**2)
if r > 10:
    score = 0      # outside the target
elif r > 5:
    score = 1      # outer circle
elif r > 1:
    score = 5      # middle circle
else:
    score = 10     # inner circle (bullseye)

print("Score is", score)

#solution...

import math

# Checks scores from the center --> edge.
def score(x_coord, y_coord):
    distance = math.sqrt(x_coord**2 + y_coord**2)
    
    if distance <= 1: return 10
    if distance <= 5: return  5
    if distance <= 10: return  1
    
    return 0