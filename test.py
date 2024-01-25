from random import random

body_coords = [(0,1)]


def eat(meal_coords):
    if body_coords[0] == meal_coords:
        body_coords.append(meal_coords)
        return random.random()
    else:
        return meal_coords
    
def move():
    pass