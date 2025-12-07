def is_invalid(num: int) -> bool:
    num_str = str(num)
    str_length = len(num_str)

    for pattern_length in range(1, str_length // 2 + 1):
        if str_length % pattern_length != 0:
            continue
        pattern = num_str[:pattern_length]

        if pattern[0] == '0':
            continue
        
        if pattern * (str_length // pattern_length) == num_str:
            return True
    
    return False


with open('./day_2/puzzle_input.txt', 'r') as f:
    puzzle_input = f.read().strip()

invalid_sum = 0

for r in puzzle_input.split(","):
    start, end = map(int, r.split("-"))
    
    invalids = [
        num for num in range(start, end + 1) if is_invalid(num)
    ]

    invalid_sum += sum(invalids)

print(invalid_sum)