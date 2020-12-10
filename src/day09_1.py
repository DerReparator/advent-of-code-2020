from typing import List
from itertools import combinations

day9_input = None

with open("input/day09_1.input", 'r') as d:
    day9_input = d.readlines()

preamble_len: int = 25
message: List[int] = [int(number) for number in day9_input]

def contains_sum(num_list: List[int], needed_sum: int) -> bool:
    for s in combinations(num_list, 2):
        if needed_sum == sum(s):
            return True
    return False


curr_idx = preamble_len

while contains_sum(message[curr_idx - preamble_len:curr_idx], message[curr_idx]):
    curr_idx = curr_idx + 1


print(f"Solution: {message[curr_idx]}")