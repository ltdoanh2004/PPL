from functools import reduce

A = [1, 2, 3, 4, 5]
sum_of_power_3 = reduce(lambda x, y: x + y**3, A)
print(f"Sum of cubes: {sum_of_power_3}")