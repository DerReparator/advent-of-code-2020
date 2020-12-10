from timeit import default_timer as timer
from typing import List

day10_input = None

input_path = "input/day10_1.input"

# read input
with open(input_path, 'r') as inp_file:
    day10_input = inp_file.readlines()
    day10_input = [int(s.strip()) for s in day10_input]

start = timer()

solution = 0
day10_input.append(0) # add the charging outlet

adapters: List[int] = sorted(day10_input)
# Add "my end device" to the list of adapters to include the last jolt difference of 3
adapters.append(adapters[-1] + 3)

no_of_1_differences = 0
no_of_3_differences = 0

for idx, adapter in enumerate(adapters[:-1]):
    if adapters[idx + 1] - adapters[idx] == 1:
        no_of_1_differences = no_of_1_differences + 1
    elif adapters[idx + 1] - adapters[idx] == 3:
        no_of_3_differences = no_of_3_differences + 1

solution = no_of_1_differences * no_of_3_differences

end = timer()
elapsed_time = end-start
print(f"Solution: {solution} in {elapsed_time}s")