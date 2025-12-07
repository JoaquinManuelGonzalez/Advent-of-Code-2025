# Logic of Resolution

## Part One

For this first part, what we can do is go through one line at a time and, for each position ``j`` (second digit of the number), find the best first digit ``a`` that appears before ``j``.

We maintain a variable ``max_left = maximum digit seen so far on the left and candidate to be the first digit of the number``, and for each ``j`` we calculate ``10 * max_left + digit[j]`` and update the maximum for the line.

As we move through the string, we update ``max_left`` with the current digit for the next positions.

Note that we use the ``ord()`` function, which returns the ASCII code of the character we send it, so we subtract ``48``, which is the ASCII code for ``0``.

## Part Two

This part acts almost as a generalisation of part one. To now obtain the **subsequence** of length ``k`` that forms the largest possible number (in our case ``k = 12``), we have to take exactly 12 digits and the number produced by the concatenation has to be the maximum possible for the sequence.

Let's propose a solution using a **stack** per line:
- We go through the digits from left to right.
- We maintain a stack with the candidate subsequence.
- When a new digit ``d`` arrives, we analyse:
    - If the top of the stack is less than the digit and there are still enough digits left to read to be able to fill up to ``k`` after doing ``pop``, then we do ``pop`` since ``d`` is a better candidate.
- We push ``d`` onto the stack as long as ``k`` final digits have not been stored. If there are more digits left, we truncate at the end to keep ``k``.
- At the end of line processing, we obtain a stack with the maximum subsequence.

