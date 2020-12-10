from timeit import default_timer as timer
from typing import List
from functools import reduce
import operator

day10_input = None

input_path = "input/day10_1_test.input"

# read input
with open(input_path, 'r') as inp_file:
    day10_input = inp_file.readlines()
    day10_input = [int(s.strip()) for s in day10_input]


def compute_fitting_successors(adapters: List[int]) -> List[int]:
    successors = [0] * (len(adapters) - 1)
    for i in range(len(successors)):
        joltage_i = adapters[i]
        if adapters[i + 1] <= joltage_i + 3:
            successors[i] = successors[i] + 1
        if i+2 < len(adapters) and adapters[i + 2] <= joltage_i + 3:
            successors[i] = successors[i] + 1
        if i+3 < len(adapters) and adapters[i + 3] <= joltage_i + 3:
            successors[i] = successors[i] + 1
    return successors + [0]

def compute_fitting_predecessors(adapters: List[int]) -> List[int]:
    predecessors = [0] * (len(adapters) - 1)
    for i in range(len(adapters)-1,-1,-1):
        joltage_i = adapters[i]
        if adapters[i - 1] >= joltage_i - 3:
            predecessors[i - 1] = predecessors[i - 1] + 1
        if i - 2 >= 0 and adapters[i - 2] >= joltage_i - 3:
            predecessors[i - 1] = predecessors[i - 1] + 1
        if i - 3 >= 0 and adapters[i - 3] >= joltage_i - 3:
            predecessors[i - 1] = predecessors[i - 1] + 1
    return [0] + predecessors

start = timer()

solution = 0
day10_input.append(0) # add the charging outlet

adapters: List[int] = sorted(day10_input)
# Add "my end device" to the list of adapters to include the last jolt difference of 3
adapters.append(adapters[-1] + 3)
successors = compute_fitting_successors(adapters)
precdecessors = compute_fitting_predecessors(adapters)

magic = map(operator.sub, successors, precdecessors) # element-wise subtraction
magic = [0 if i < 0 else i for i in magic]

print(f"Sorted input: {adapters}")
print(f"Successors:   {successors}")
print(f"Predecessors: {precdecessors}")

solution = reduce(lambda x, y: x*y, [i for i in magic if i > 0])

end = timer()
elapsed_time = end-start
print(f"Solution: {solution} in {elapsed_time}s")