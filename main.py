from time import sleep
from typing import Dict
from random import randint
import os
import platform


def cooking_meal(x: int, y: int):
    fruit = {'x': randint(0, x - 1), 'y': randint(0, y - 1)}
    return fruit

def eat(fruit, body_coords):
    if body_coords[0]['x'] == fruit['x'] and body_coords[0]['y'] == fruit['y']:
        pass #TODO

def move(body_coords: list[tuple], vector: str):
  '''
  body_coords - coords of body and head (body_coords[0]);
  vector - direction of move.

  Function for change body and head position.
  '''
  if vector == 'down':
    body_coords.insert(0, (body_coords[0][0], body_coords[0][1] + 1))
    body_coords.pop()
  elif vector == 'up':
    body_coords.insert(0, (body_coords[0][0], body_coords[0][1] - 1))
    body_coords.pop()
  elif vector == 'right':
    body_coords.insert(0, (body_coords[0][0], body_coords[0][0] + 1))
    body_coords.pop()
  elif vector == 'left':
    body_coords.insert(0, (body_coords[0][0], body_coords[0][0] - 1))
    body_coords.pop()
  return body_coords
print('hello')
    
def check_symbols(head_symbol: str, field_symbol: str, error_text='Невидимая змейка'):
    if field_symbol == head_symbol:
        raise ValueError(error_text)

def body_raise(body_coords: list[Dict]):
    body_coords.append(body_coords[0])

def create_field(body_coords: list[Dict],
                 fruit: dict[str: int],
                 X: int, Y: int,
                 head_symbol='%',
                 field_symbol='+'):
    '''
    Function for print game field.
    '''
    check_symbols(head_symbol, field_symbol)
    
    ground = list()
    for x in range(X):
        tmp = list()
        for y in range(Y):
            if x == body_coords[0]['x'] and y == body_coords[0]['y']:
                tmp.append(head_symbol)
            elif x == fruit['x'] and y == fruit['y']:
                tmp.append('@')
            elif body_coords[0]['x'] == fruit['x'] and body_coords[0]['y'] == fruit['y']:
                body_raise()
                tmp.append('#')
            else:
                tmp.append(field_symbol)
        ground.append(tmp)
    return ground

def clear():
    platf = platform.system()
    if platf == 'Windows':
        os.system('cls')
    elif platf == 'Linux':
        os.system('clear')
        
def print_field(field):
    for i in field:
        print(*i)

BODY_COORDS = [{'x': 5, 'y': 5}]
VECTOR = 'right'
X = 15
Y = 15

def run(game_speed: float):
    FRUIT = cooking_meal(x=X, y=Y)
    while BODY_COORDS[0]['x'] < X and BODY_COORDS[0]['y'] < Y:
        clear()
        if BODY_COORDS[0]['x'] == FRUIT['x'] and BODY_COORDS[0]['y'] == FRUIT['y']:
            FRUIT = cooking_meal(X, Y)
        FIELD = create_field(body_coords=BODY_COORDS, X=X, Y=Y, fruit=FRUIT)
        move(BODY_COORDS, VECTOR)
        print_field(FIELD)
        sleep(game_speed)
    print('You lose this game!')


    # print(BODY_COORDS[0]['x'] < X)
run(0.2)