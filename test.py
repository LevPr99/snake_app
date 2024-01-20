ground = list()

for i in range(10):
    tmp = list()
    for j in range(10):
        tmp.append('*')
    ground.append(tmp)

print(*ground, sep='\n')