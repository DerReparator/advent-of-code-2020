day5_input = None

input_path = "input/day05_1.input"

# read input
with open(input_path, 'r') as inp_file:
    day5_input = inp_file.readlines()
    day5_input = ''.join(day5_input)

parsed_input = [seat for seat in  day5_input.split('\n')]

def get_id(id_string: str, high_char: str, low_char: str):
    ret = id_string.replace(high_char, '1')
    ret = ret.replace(low_char, '0')
    return int(ret, 2)

def computeSeatId(row: int, col: int):
    return row * 8 + col
    
seatIDs = [computeSeatId(get_id(seat[:7], 'B', 'F'), get_id(seat[-3:], 'R', 'L')) for seat in parsed_input]

print(f"Highest Seat ID={max(seatIDs)}")
