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

# Day 4_2
pattern_hair_color = re.compile("^#[\da-f]{6}$")
valid_eye_colors = set(["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])
pattern_passport_id = re.compile("^\d{9}$")

def check_height_is_valid(hgt):
    if re.match("^\d{3}cm$", hgt):
        if 150 <= int(hgt[:-2]) <= 193:
            return True
    elif re.match("^\d{2}in$", hgt):
        if 59 <= int(hgt[:-2]) <= 76:
            return True
    return False

# Parse input
parsed_input = day4_input.split("\n\n")
parsed_input = [re.split(r'\s', npc) for npc in parsed_input]

for j, npc in enumerate(parsed_input):
    for i in range(len(npc)):
        npc[i] = tuple(npc[i].split(":"))
    parsed_input[j] = {key: value for (key,value) in parsed_input[j]}

for npc in parsed_input:
    if all(key in npc for key in needed_keys):
        if not 1920 <= int(npc["byr"]) <= 2002:
            continue
        if not 2010 <= int(npc["iyr"]) <= 2020:
            continue
        if not 2020 <= int(npc["eyr"]) <= 2030:
            continue
        if not check_height_is_valid(npc["hgt"]):
            continue
        if not bool(pattern_hair_color.match(npc["hcl"])):
            continue
        if npc["ecl"] not in valid_eye_colors:
            continue
        if not bool(pattern_passport_id.match(npc["pid"])):
            continue
        nr_valid_npcs = nr_valid_npcs + 1
        
        
print(f"#valid NPCs: {nr_valid_npcs}")
