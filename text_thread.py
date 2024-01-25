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
def print_to_console1(text, **kwargs):
    if 'sep' in kwargs and 'text' in kwargs:
        print(kwargs['text'], kwargs['sep'])

print_to_console1(text='123', sep='\n\n\n')