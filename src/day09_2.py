from typing import List
from itertools import combinations, permutations

day9_input = None

with open("input/day09_1.input", 'r') as d:
    day9_input = d.readlines()

SOLUTION_FROM_PART_1 = 88311122

message: List[int] = [int(number) for number in day9_input]

for i in range(len(message)):
    for j in range(i, len(message)):
        curr_sum = sum(message[i:j])
        if curr_sum > SOLUTION_FROM_PART_1:
            break
        elif curr_sum == SOLUTION_FROM_PART_1:
            print(f"Solution: {min(message[i:j]) + max(message[i:j])}")
            exit(0)

