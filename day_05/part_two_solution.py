def merge_ranges(ranges: list) -> list:
    # Sort ranges by their start values
    ranges.sort()
    merged = []

    for start, end in ranges:
        # If merged is empty or there is no overlap, add the range
        if not merged or start > merged[-1][1] + 1:
            merged.append([start, end])
        else:
            # There is overlap, so we merge the ranges
            merged[-1][1] = max(merged[-1][1], end)
    
    return merged


with open('./day_05/puzzle_input.txt', 'r') as f:
    puzzle_input = f.read()

list_of_fresh_ids = puzzle_input.strip().split("\n\n")[0]

# Parse ranges of fresh product IDs
ranges = []
for id_range in list_of_fresh_ids.splitlines():
    start, end = map(int, id_range.split('-'))
    ranges.append((start, end))

# Fuse ranges
merged_ranges = merge_ranges(ranges)

# Count Fresh Ids
count_of_fresh_ids = sum(end - start + 1 for start, end in merged_ranges)

print(count_of_fresh_ids)