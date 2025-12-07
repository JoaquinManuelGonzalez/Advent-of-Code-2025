with open('./day_01/puzzle_input.txt', 'r') as f:
    puzzle_input = f.read()

dial = 50
zero_counter = 0

for line in puzzle_input.splitlines():
    rotation = line[0]
    distance = int(line[1:])
    
    turns = distance // 100
    remainder = distance % 100

    if rotation == 'L':
        if dial > 0 and remainder >= dial:
            turns += 1
        dial = (dial - remainder) % 100
    else:
        if dial + remainder >= 100:
            turns += 1
        dial = (dial + remainder) % 100
    
    zero_counter += turns

print(zero_counter)