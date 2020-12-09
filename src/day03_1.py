day3_input = None

# read input
with open("input/day03_1.input", 'r') as inp_file:
    day3_input = inp_file.readlines()
    day3_input = [s.strip() for s in day3_input]

nr_trees = 0

hill_map = day3_input
x = 0
y = 0
while y < len(hill_map):
    if hill_map[y][x] == '#':
        nr_trees = nr_trees + 1
    x = (x + 3) % len(hill_map[0])
    y = y + 1

print(f"Solution: {nr_trees}")