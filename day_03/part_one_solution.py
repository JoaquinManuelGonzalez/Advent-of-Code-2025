def max_joltage_of_bank(line: str) -> int:
    digits = [ord(char) - 48 for char in line.strip()] # Convert char to int
    max_left = digits[0]
    best = -1

    for j in range(1, len(digits)):
        val = 10 * max_left + digits[j]
        if val > best:
            best = val
        if digits[j] > max_left:
            max_left = digits[j]

    return best


with open('./day_03/puzzle_input.txt', 'r') as f:
    puzzle_input = f.read()

total_joltage = 0

for line in puzzle_input.splitlines():
    line = line.strip()
    total_joltage += max_joltage_of_bank(line)

print(total_joltage)