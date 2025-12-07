# Logic of Resolution

## Part One

To solve the problem, we will have to consider the following for each **range A-B**:
1. We generate all the numbers in that specified range.
2. We convert the generated number to a string and see if the string number meets these two properties:
    - The length of the string is even (note that if it is odd, there is no pattern that can be repeated).
    - The first half of the number is equal to the second half.
3. We save the numbers that meet these conditions.
4. We add up all the invalid IDs from all ranges.

## Part Two

Now that an ID is invalid if **it consists solely of a pattern ``P`` repeated at least twice**, we can solve the problem as follows:
1. Convert the number to a string.
2. Test possible lengths for the pattern P (note that P cannot be longer than half the length of the string, as it cannot be repeated twice).
3. We see if the number has a length that is a multiple of the length of the pattern we are testing. If a pattern does not fit the total length, it is discarded.
4. We obtain the possible base for the pattern by taking ``X`` number of digits from the number, where ``X`` is the length we are testing for the pattern.
5. Patterns with ``0`` on the left are discarded since IDs do not have leading zeros.
6. We construct the repeated number considering the digits we took for the pattern, i.e., for example, if our pattern is ``12`` and we see that it can fit ``5`` times in the length of the number, we do: ``P * repetitions → "12" * 5 → "1212121212"``
7. We compare with the original number. If the pattern matches the number, then the ID is invalid.