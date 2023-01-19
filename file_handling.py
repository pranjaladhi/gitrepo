my_shapes = ["square", "circle", "triangle"]

with open('shapes.txt', 'w') as w:
    for shape in my_shapes:
        w.write(shape)

print("test")
