# from threading import Thread
# from time import sleep


# def ground():
#     i = 0
#     while True:
#         if i == 100:
#             break
#         i += 1
#         print(i)
#         sleep(1.5)

# t1 = Thread(target=ground)
# t2 = Thread(target=ground)
# t1.start()
# t2.start()
# t1.join(timeout=5.0)

body_coords = [(0,0), (0,1), (0,2)]

for xy in range(len(body_coords)): # from 0 to 3 - 1
    # print(body_coords[xy])
    for j in body_coords[xy]:
        print(j)
    print()