import bisect


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


def is_fresh(merged_ranges: list, product_id: int) -> bool:
    # bisect_right finds the point where we would insert [x, +inf] to maintain order
    i = bisect.bisect_right(merged_ranges, [product_id, float('inf')]) - 1

    if i >= 0:
        start, end = merged_ranges[i]
        return start <= product_id <= end
    return False

with open('./day_05/puzzle_input.txt', 'r') as f:
    puzzle_input = f.read()

list_of_fresh_ids, list_of_products = puzzle_input.strip().split("\n\n")

# Parse ranges of fresh product IDs
ranges = []
for id_range in list_of_fresh_ids.splitlines():
    start, end = map(int, id_range.split('-'))
    ranges.append((start, end))

# Parse product IDs
ids_of_products = list(map(int, list_of_products.splitlines()))

# Fuse ranges
merged_ranges = merge_ranges(ranges)

# Count Fresh Ids
count_of_fresh_ids = sum(is_fresh(merged_ranges, product) for product in ids_of_products)

print(count_of_fresh_ids)