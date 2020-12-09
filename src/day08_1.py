from collections import defaultdict

day8_input = None

input_path = "input/day08_1.input"

# read input
with open(input_path, 'r') as inp_file:
    day8_input = inp_file.readlines()
    day8_input = [s.strip() for s in day8_input]

program = [instr.split(' ') for instr in day8_input]

# Registers
accu = 0
ip = 0

trace = [0] * len(program)


# CPU
while trace[ip] == 0:
    trace[ip] = 1
    # Decode
    operator = program[ip][0]
    data = int(program[ip][1][1:])
    if program[ip][1][0] == '-':
        data = data * -1
    
    # Execute
    if operator == 'nop':
        ip = ip + 1
        continue
    elif operator == 'acc':
        ip = ip + 1
        accu = accu + data
        continue
    elif operator == 'jmp':
        ip = ip + data
        continue

# Here, an already executed instruction was encountered

print(f"Solution: {accu}")