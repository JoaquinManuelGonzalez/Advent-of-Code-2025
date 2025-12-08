def count_adjacent_at(i: int, j: int, puzzle_grid: list, possible_directions: list) -> int:
    adjacent_count = 0

    for dir_row, dir_col in possible_directions:
        new_row = i + dir_row
        new_col = j + dir_col
        if 0 <= new_row < len(puzzle_grid) and 0 <= new_col < len(puzzle_grid[i]):
            if puzzle_grid[new_row][new_col] == '@':
                adjacent_count += 1
    
    return adjacent_count

with open('./day_04/puzzle_input.txt', 'r') as f:
    puzzle_input = f.read()
    
accesible = 0
puzzle_grid = [
    list(line) for line in puzzle_input.splitlines()
]
possible_directions = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1)
]

for i in range(len(puzzle_grid)):
    for j in range(len(puzzle_grid[i])):
        if puzzle_grid[i][j] == '@':
            if count_adjacent_at(i, j, puzzle_grid, possible_directions) < 4:
                accesible += 1

print(accesible)