distance = lambda x1, y1, x2, y2: ((x1 - x2)**2 + (y1 - y2)**2)**0.5

x1, y1 = 3, 4
x2, y2 = 7, 1
dst = distance(x1, y1, x2, y2)
print(f"Distance: {dst}")
