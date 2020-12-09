day3_input = None

# read input
with open("input/day03_1.input", 'r') as inp_file:
    day3_input = inp_file.readlines()
    day3_input = [s.strip() for s in day3_input]

solution = 1 # 1 because we will multiply values cumulatively
hill_map = day3_input

def check_slope(x_off: int, y_off: int):
    nr_trees = 0
    x = 0
    y = 0
    while y < len(hill_map):
        if hill_map[y][x] == '#':
            nr_trees = nr_trees + 1
        x = (x + x_off) % len(hill_map[0])
        y = y + y_off
    return nr_trees

solution = solution * check_slope(1, 1)
solution = solution * check_slope(3, 1)
solution = solution * check_slope(5, 1)
solution = solution * check_slope(7, 1)
solution = solution * check_slope(1, 2)


print(f"Solution: {solution}")