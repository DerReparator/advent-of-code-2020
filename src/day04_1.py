import re

day4_input = None

input_path = "input/day04_1.input"

# read input
with open(input_path, 'r') as inp_file:
    day4_input = inp_file.readlines()
    day4_input = ''.join(day4_input)


# All needed keys
needed_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

nr_valid_npcs = 0

# Parse input
parsed_input = day4_input.split("\n\n")
parsed_input = [re.split(r'\s', npc) for npc in parsed_input]

for j, npc in enumerate(parsed_input):
    for i in range(len(npc)):
        npc[i] = tuple(npc[i].split(":"))
    parsed_input[j] = {key: value for (key,value) in parsed_input[j]}

for npc in parsed_input:
    if all(key in npc for key in needed_keys):
        nr_valid_npcs = nr_valid_npcs + 1
        
print(f"#valid NPCs: {nr_valid_npcs}")
