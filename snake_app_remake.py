import os
import platform
from enum import Enum
from random import randint


class Difficult(Enum):
    
    Easy = 1.1
    Medium = 0.5
    Hard = 0.2


class Unit:
    
    def __init__(self, symbol, x=0, y=0):
        self._x = x
        self._y = y
        self.symbol = symbol
        
    def __call__(self):
        return (self._x, self._y, )
    
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, value):
        self._x = value
        
    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, value):
        self._y = value


class Snake(Unit):

    def __init__(self, head_symbol, body_symbol, x, y):
        super().__init__(body_symbol, x, y)
        self.head_symbol = head_symbol
        self.snake_body_coords = [(self._x, self._y)]

    def to_eat(self, meal):
        if self.snake_body_coords[0][0] == meal.x and self.snake_body_coords[0][1] == meal.y:
            self.snake_body_coords.append((meal.x, meal.y, ))
    
    def move(self, vector):
        '''
        body_coords - coords of body and head (body_coords[0]);
        vector - direction of move.

        Function for change body and head position.
        '''
        if vector == 'down':
            self.snake_body_coords.insert(0, (self.snake_body_coords[0][0], self.snake_body_coords[0][1] + 1))
            self.snake_body_coords.pop()
        elif vector == 'up':
            self.snake_body_coords.insert(0, (self.snake_body_coords[0][0], self.snake_body_coords[0][1] - 1))
            self.snake_body_coords.pop()
        elif vector == 'right':
            self.snake_body_coords.insert(0, (self.snake_body_coords[0][0] + 1, self.snake_body_coords[0][1]))
            self.snake_body_coords.pop()
        elif vector == 'left':
            self.snake_body_coords.insert(0, (self.snake_body_coords[0][0] - 1, self.snake_body_coords[0][1]))
            self.snake_body_coords.pop()
        return self.snake_body_coords
    
    def __len__(self):
        return len(self.snake_body_coords)
    

class Meal(Unit):
    
    def cooking_meal(self, area_length, area_width):
        self.x = randint(0, area_length - 1)
        self.y = randint(0, area_width - 1)


class GameArea:
    
    def __init__(self, length=10, width=10, area_symbol='*'):
        self._length = length
        self._width = width
        self._area_symbol = area_symbol
        self.game_area = []
    
    def create_area(self):
        self.game_area = []
        for y in range(self._length):
            tmp = []
            for x in range(self._width):
                tmp.append(self._area_symbol)
            self._game_area.append(tmp)
    
    def add_snake(self, snake):
        for i, v in enumerate(snake.snake_body_coords):
            if i == 0:
                self.game_area[v[0]][v[1]] = snake.head_symbol
            else:
                self.game_area[v[0]][v[1]] = snake.symbol
            
    def add_meal(self, meal):
        food = meal()
        self.game_area[food[0]][food[1]] = meal.symbol
        
    def check_snake_coords(self, snake):
        if 0 > snake.snake_body_coords[0][0] or 0 > snake.snake_body_coords[0][1] or \
            snake.snake_body_coords[0][0] > self._length or snake.snake_body_coords[0][1] > self._length:
            return False
        else:
            return True
        

    def clear(self):
        """Function for clear console. If os == Windows, call command 'cls'.
        if os == Linux, call 'clear'
        """
        platf = platform.system()
        if platf == 'Windows':
            os.system('cls')
        elif platf == 'Linux':
            os.system('clear')


class KeyHandler:
    
    def __init__(self):
        pass
    

class SnakeGame:
    
    @staticmethod
    def print_area(area):
        print(*area.game_area, sep='\n')

area = GameArea()
snake = Snake('%', '#', 0, 0)
snake.snake_body_coords = [(1,1), (1,2), (1,3)]
meal = Meal('@')

area.create_area()
area.add_snake(snake=snake)
meal.cooking_meal(10, 10)
area.add_meal(meal)
area.print_area()
