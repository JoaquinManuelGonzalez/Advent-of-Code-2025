from collections import deque


with open('./day_04/puzzle_input.txt', 'r') as f:
    puzzle_input = f.read()
    
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
neighbor_count = [
    [0]*len(puzzle_grid[0]) for _ in range(len(puzzle_grid))
]

for i in range(len(puzzle_grid)):
    for j in range(len(puzzle_grid[i])):
        if puzzle_grid[i][j] == '@':
            count = 0
            for dir_row, dir_col in possible_directions:
                new_row = i + dir_row
                new_col = j + dir_col
                if 0 <= new_row < len(puzzle_grid) and 0 <= new_col < len(puzzle_grid[i]):
                    if puzzle_grid[new_row][new_col] == '@':
                        count += 1
            neighbor_count[i][j] = count

queue = deque()
in_queue = [
    [False]*len(puzzle_grid[0]) for _ in range(len(puzzle_grid))
]

for i in range(len(puzzle_grid)):
    for j in range(len(puzzle_grid[i])):
        if puzzle_grid[i][j] == '@' and neighbor_count[i][j] < 4:
            queue.append((i, j))
            in_queue[i][j] = True

total_removed = 0

while queue:
    i, j = queue.popleft()
    in_queue[i][j] = False
    # if already removed, skip
    if puzzle_grid[i][j] != '@':
        continue
    # remove '@'
    puzzle_grid[i][j] = '.'
    total_removed += 1
    # update neighbors
    for dir_row, dir_col in possible_directions:
        new_row = i + dir_row
        new_col = j + dir_col
        if 0 <= new_row < len(puzzle_grid) and 0 <= new_col < len(puzzle_grid[i]):
            if puzzle_grid[new_row][new_col] == '@':
                # decrement neighbor count
                neighbor_count[new_row][new_col] -= 1
                # if now is accessible and not already in queue, add to queue
                if neighbor_count[new_row][new_col] < 4 and not in_queue[new_row][new_col]:
                    queue.append((new_row, new_col))
                    in_queue[new_row][new_col] = True

print(total_removed)