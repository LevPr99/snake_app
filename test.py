def eat(body_coords: list[tuple], fruit):
    return (body_coords[0][0], body_coords[0][1] + len(body_coords), )

body = [(0, 1)]
body.append(eat(body, (0, 1)))
body.append(eat(body, (0, 1)))
body.append(eat(body, (0, 1)))
print(body)