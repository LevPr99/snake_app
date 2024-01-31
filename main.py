from time import sleep
from random import randint
import os
import platform
from enum import Enum
from art import tprint
import keyboard


def cooking_meal(x: int, y: int) -> tuple:
    """Function for change fruit coord.

    Args:
        x (int): Coord x for fruit position
        y (int): Coord y for fruit position

    Returns:
        tuple: New tuple with coords of fruit
    """
    fruit = (randint(0, x - 1), randint(0, y - 1))
    return fruit

def eat(fruit):
    pass  #TODO

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
    body_coords.insert(0, (body_coords[0][0] + 1, body_coords[0][1]))
    body_coords.pop()
  elif vector == 'left':
    body_coords.insert(0, (body_coords[0][0] - 1, body_coords[0][1]))
    body_coords.pop()
  return body_coords
print('hello')
    
def check_symbols(head_symbol: str, field_symbol: str, error_text='Невидимая змейка'):
    if field_symbol == head_symbol:
        raise ValueError(error_text)

# def body_raise(body_coords: list[tuple]):
#   body_coords.append(body_coords[0])

def create_field(body_coords: list[tuple], fruit: tuple, 
                 X: int, Y: int, head_symbol='%', field_symbol=' '):
    '''
    Function for print game field.
    '''
    check_symbols(head_symbol, field_symbol)

    ground = list()
    for y in range(Y):
        tmp = list()
        for x in range(X):
            if x == body_coords[0][0] and y == body_coords[0][1]:
                tmp.append(head_symbol)
            elif x == fruit[0] and y == fruit[1]:
                tmp.append('@')
            elif body_coords[0][0] == fruit[0] and body_coords[0][1] == fruit[1]:
                eat(fruit)
                tmp.append('#')
            else:
                tmp.append(field_symbol)
        ground.append(tmp)
    return ground

def clear():
    """Function for clear console. If os == Windows, call command 'cls'.
    if os == Linux, call 'clear'
    """
    platf = platform.system()
    if platf == 'Windows':
        os.system('cls')
    elif platf == 'Linux':
        os.system('clear')
        
def print_field(field):
    out_s = ''
    for i in field:
        out_s += ''.join(i).ljust(10) + '\n'
    print(out_s)
    
class Difficult(Enum):
    
    Easy = 1.1
    Medium = 0.5
    Hard = 0.2

def game_over():
    tprint('You Lose!', font='rnd-xlarge')


BODY_COORDS = [(4, 6)]
VECTOR = 'right'
X = 15
Y = 15

def run(game_speed: Difficult):
    FRUIT = cooking_meal(x=X, y=Y)
    while 0 <= BODY_COORDS[0][0] < X and 0 <= BODY_COORDS[0][1] < Y:
        clear()
        if BODY_COORDS[0][0] == FRUIT[0] and BODY_COORDS[0][1] == FRUIT[1]:
            FRUIT = cooking_meal(X, Y)
        FIELD = create_field(body_coords=BODY_COORDS, X=X, Y=Y, fruit=FRUIT, field_symbol='*')
        move(BODY_COORDS, VECTOR)
        print_field(FIELD)
        sleep(game_speed)
    clear()
    game_over()


# run(Difficult.Hard.value)