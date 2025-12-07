def max_subsequence_of_length_k(digits: list[int], k: int) -> list[int]:
    n = len(digits)
    stack = []
    to_remove = n - k  # Amount of digits we can remove

    for d in digits:
        # While we can remove digits and the last digit in the stack is less than the current digit
        while stack and to_remove > 0 and stack[-1] < d:
            stack.pop()
            to_remove -= 1
        stack.append(d)

    # If we still have to remove digits, remove from the end
    return stack[:k]

def max_joltage_of_bank(line: str, k: int) -> int:
    battery_bank = line.strip()
    digits = [int(c) for c in battery_bank]
    best_digits = max_subsequence_of_length_k(digits, k)
    
    val = 0
    for d in best_digits:
        val = val * 10 + d

    return val

with open('./day_03/puzzle_input.txt', 'r') as f:
    puzzle_input = f.read()

total_joltage = 0

for line in puzzle_input.splitlines():
    line = line.strip()
    total_joltage += max_joltage_of_bank(line, 12)

print(total_joltage)