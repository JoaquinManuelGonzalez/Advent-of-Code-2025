# Logic of Resolution

## Part One

For this first part, I decided to store the input in a list of lists representing each row and, within the rows, all the columns.

Once this is done, we have to represent the eight **adjacent** directions that an element can have. We can see it this way:

```
(-1, -1), (-1, 0), (-1, 1),
(0, -1),         , (0, 1),
(1, -1), (1, 0), (1, 1)
```

Note that not all elements can have their 8 adjacent neighbours. A clear example of this are the elements at the ends of the grid, which have ``3`` each, so it is important to check that we always access valid positions.

With all this in mind, all that remains is to go through the grid and count for each element whether the number of neighbouring rolls is less than ``4``, in which case we count it.

## Part Two

For this second part, I initially thought of a much more iterative solution than the one I ended up implementing. At first glance, I noticed that I could generate passes to the roll grid where, for each pass, I would search for all accessible rolls, remove them, count how many were removed, and repeat this process until no more could be removed in any pass. This is correct, but it can be optimised.

To optimise it, I researched and noticed that I could use a BFS/queue-type solution with duplicate element control. This new solution consists of:
1. Counting neighbours for all rolls.
2. Creating the structures for BFS:
    - A queue to store the rolls to be removed.
    - A Boolean array to mark whether a roll has already been queued.
3. Queue all initial accessible rolls.
4. Start the BFS loop:
    - Check whether the current roll still exists.
    - Remove the current roll and count it.
    - Update the neighbours so that if the quantity is now < 4, the neighbour is glued.
    - Repeat until there are no accessible rolls, i.e. the queue is empty.

In this way, we can handle a **linear complexity O(N)** for the solution.
