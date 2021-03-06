from collections import defaultdict

day7_input = None

input_path = "input/day07_1.input"
# input_path = "input/day07_1_test.input"

# read input
with open(input_path, 'r') as inp_file:
    day7_input = inp_file.readlines()
    day7_input = [s.strip() for s in day7_input]

bag_rules = {}
bag_is_contained_in = defaultdict(list)
contains_shiny_gold = set() # The length of this set will be the solution

def parse_color(first_part: str, second_part: str):
    return first_part + " " + second_part

# Parse input
for rule in day7_input:
    words = rule.split(" ")
    color = parse_color(words[0], words[1])
    contained_bags = []
    if words[4] == 'no':
        if color not in bag_rules:
            bag_rules[color] = []
    else:
        idx_of_bag = 7
        while idx_of_bag < len(words):
            # There's still a contained bag to be parsed
            contained_bags.append(tuple([int(words[idx_of_bag - 3]), parse_color(words[idx_of_bag - 2], words[idx_of_bag - 1])]))
            idx_of_bag = idx_of_bag + 4
        bag_rules[color] = contained_bags
        for amount, contained_bag in contained_bags:
            bag_is_contained_in[contained_bag].append(color)

print("Bag Rules:")
for idx, color_name in enumerate(bag_rules):
    print(f"{idx} - {color_name} : {bag_rules[color_name]}")

print("Contained-in Rules:")
for idx, color_name in enumerate(bag_is_contained_in):
    print(f"{idx} - {color_name} : {bag_is_contained_in[color_name]}")



# now query the rules with shiny gold
def traverse_up(color: str):
    for container in bag_is_contained_in[color]:
        if container not in contains_shiny_gold:
            contains_shiny_gold.add(container)
            traverse_up(container)

traverse_up("shiny gold")

print(f"Solution: {len(contains_shiny_gold)}")
for bag in sorted(contains_shiny_gold):
    print(bag)