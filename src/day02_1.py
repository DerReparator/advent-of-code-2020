day2_input = None

# read input
with open("input/day02_1.input", 'r') as inp_file:
    day2_input = inp_file.readlines()
    day2_input = [s.strip() for s in day2_input]

nr_valid_passwds = 0

db_entries = [entry.split(' ') for entry in day2_input]
for idx, entry in enumerate(db_entries):
    entry[0] = tuple([int(i) for i in entry[0].split('-')])
    entry[1] = entry[1][0]

for entry in db_entries:
    if entry[0][0] <= entry[2].count(entry[1]) <= entry[0][1]:
        nr_valid_passwds = nr_valid_passwds + 1

print(f"Solution: {nr_valid_passwds}")