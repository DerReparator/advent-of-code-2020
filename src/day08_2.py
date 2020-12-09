import time
import logging
from logging import debug

# Configure logging
logging.basicConfig(format='%(asctime)s [%(levelname)s]: %(message)s', level=logging.INFO)

day8_input = None

input_path = "input/day08_1.input"

# read input
with open(input_path, 'r') as inp_file:
    day8_input = inp_file.readlines()
    day8_input = [s.strip() for s in day8_input]

last_instr_changed_idx = 0

program = [instr.split(' ') for instr in day8_input]

# Registers
accu = 0
ip = 0

prg_step = 1

def modify_program_code():
    '''Modify program code according to Day 8, Part 2.
    
    Start searching for changeable instructions from global variable 
    '''
    global last_instr_changed_idx
    # time.sleep(0.1)

    #if last_instr_changed_idx > 0: # First, change back previous change
    swap_nop_jmp_instr(last_instr_changed_idx)
    last_instr_changed_idx = last_instr_changed_idx + 1 # Search starting from the next adress
    # Then search for next changeable instruction and swap it
    for i, instr in enumerate(program[last_instr_changed_idx:], last_instr_changed_idx):
        if instr[0] in ("nop", "jmp"):
            last_instr_changed_idx = i
            swap_nop_jmp_instr(i)
            break

def swap_nop_jmp_instr(ip: int):
    '''Swap the instruction at "ip" if its either NOP or JMP'''
    if ip <= 0:
        return
    if program[ip][0] == "nop":
        program[ip][0] = "jmp"
        debug(f"Changing instruction at {ip} from NOP to JMP")
    elif program[ip][0] == "jmp":
        program[ip][0] = "nop"
        debug(f"Changing instruction at {ip} from JMP to NOP")

while ip != len(program):
    ip = 0
    accu = 0
    trace = [0] * len(program)
    prg_step = 1
    modify_program_code()
    debug(f"Executing after change at {last_instr_changed_idx}")
    # CPU
    while ip < len(program) and trace[ip] == 0:
        trace[ip] = prg_step
        prg_step = prg_step + 1
        # Decode
        operator = program[ip][0]
        data = int(program[ip][1][1:])
        if program[ip][1][0] == '-':
            data = data * -1

        # Execute
        if operator == 'nop':
            ip = ip + 1
        elif operator == 'acc':
            ip = ip + 1
            accu = accu + data
        elif operator == 'jmp':
            ip = ip + data
    debug(f"Execution finished. Trace: {trace}")

# Here, the program terminated gracefully
print(f"Solution: {accu}")
