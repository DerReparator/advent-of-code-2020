from collections import defaultdict
from string import ascii_lowercase

day6_input = None

input_path = "input/day06_1.input"

# read input
with open(input_path, 'r') as inp_file:
    day6_input = inp_file.readlines()
    day6_input = ''.join(day6_input)

test_input = '''abc

a
b
c

ab
ac

a
a
a
a

b'''

parsed_input = day6_input.split('\n\n')

yes_answers = []
for group_answer in parsed_input:
    nr_of_yes = 0
    nr_of_persons = 0
    occurences = defaultdict(int)
    for s in group_answer.split('\n'):
        nr_of_persons = nr_of_persons + 1
        for c in s:
            occurences[c] = occurences[c] + 1
    for c in ascii_lowercase:
        if occurences[c] == nr_of_persons:
            nr_of_yes = nr_of_yes + 1
    yes_answers.append(nr_of_yes)
    
print(f"# of 'yes', that everybody from a group answered: {sum(yes_answers)}")
