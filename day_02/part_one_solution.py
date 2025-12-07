def is_invalid(num: int) -> bool:
    num_str = str(num)
    
    if len(num_str) % 2 != 0:
        return False

    mid = len(num_str) // 2
    return num_str[:mid] == num_str[mid:]

with open('./day_02/puzzle_input.txt', 'r') as f:
    puzzle_input = f.read()

invalid_sum = 0

for num_range in puzzle_input.split(","):
    start, end = map(int, num_range.split("-"))
    
    invalids = [
        num for num in range(start, end + 1) if is_invalid(num)
    ]

    invalid_sum += sum(invalids)

print(invalid_sum)