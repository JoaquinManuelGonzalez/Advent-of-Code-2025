with open('./day_1/puzzle_input.txt', 'r') as f:
    puzzle_input = f.read()

dial = 50
zero_counter = 0

for line in puzzle_input.splitlines():
    rotation = line[0]
    distance = int(line[1:])

    if rotation == 'L':
        dial = (dial - distance) % 100
    else:
        dial = (dial + distance) % 100

    if dial == 0:
        zero_counter += 1
    
print(zero_counter)