# from time import sleep


def move(head, body_coords, vector):
    '''
    head - head coords;
    body_coords;
    vector - direction of our move.
    
    Function for change body and head position.
    '''
    if len(body_coords) > 0:
        if vector == 'down':
            for indx in range(len(body_coords)):
                for _ in body_coords[indx]:
                    body_coords[indx][1] += 1
                    head[indx][1] += 1
        elif vector == "right":
            for indx in range(len(body_coords)):
                for _ in body_coords[indx]:
                    body_coords[indx][0] += 1
                    head[indx][0] += 1
        elif vector == "left":
            for indx in range(len(body_coords)):
                for _ in body_coords[indx]:
                    body_coords[indx][0] -= 1
                    head[indx][1] -= 1
        elif vector == "up":
            for indx in range(len(body_coords)):
                for _ in body_coords[indx]:
                    body_coords[indx][0] -= 1
                    head[indx][0] -= 1


# def change_coords(**kwargs):
#     for indx in range(len(body_coords)):
#             for _ in body_coords[indx]:
#                 body_coords[indx][1] += 1
#                 head[indx][1] += 1
                
# change_coords(actions[0])



def print_field(head_coord: list, body_coord: list, field_size=10, head_symbol='%', field_symbol='#'):
    '''
    Function for print game field.
    '''
    
    if head_symbol == field_symbol:
        raise ValueError('Невидимая змейка')
        
    ground = list()
    for x in range(field_size):
        tmp = list()
        for y in range(10):
            if x == head_coord[0] and y == head_coord[1]:
                tmp.append('%')
            else:
                tmp.append('#')
        ground.append(tmp)
    
    print(*ground, sep='\n')
    print()


VECTOR = 'right'
HEAD_COORDS = (5, 5)
BODY_COORDS = []


print_field((1, 0), head_symbol='@', field_symbol='@')