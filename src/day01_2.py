day1_input = None

# read input
with open("input/day01_1.input", 'r') as inp_file:
    day1_input = inp_file.readlines()
    day1_input = [int(s.strip()) for s in day1_input]

for i in day1_input:
    for j in day1_input:
        for k in day1_input:
            if i + j + k == 2020:
                print(f"Solution: {i * j * k}")
                exit(0)