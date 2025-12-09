# Logic of Resolution

## Part One

We take the list of fresh product ID ranges and the list of available product IDs. The first thing to analyse is the list of fresh product ID ranges, as there may be overlapping ranges. To do this, we will merge the overlapping ranges. First, we sort each range by its start and take two things into account:
1. If the current range does not touch or overlap the last merged range → it is added as a new interval.
2. If it does overlap, it is joined by extending the end of the last merged range.

This gives us the **non-overlapping ranges**, which makes comparison easier.

Now we have to search for whether each available product ID is in any of the ranges, but there is one detail we can take advantage of: to merge, we had to sort the ranges by their start, which means that once we obtain the list of non-overlapping ranges, it is also sorted, allowing us to perform a **binary search**.

This search will tell us in which range the ID *could* be contained. Once we obtain the start and end of that interval, we just have to check if the ID is between them. If so, it is fresh; if not, it is not.

## Part Two

Now we no longer care about the list of available product IDs, which makes our job a little easier. We have to focus on the question: How many IDs in **total** cover the fresh ID ranges?

To answer this, we will first perform the same merge as before, which allows us to work with a list of non-overlapping ranges that is also sorted.

Then, for each range in that list, we just have to check the **length** of that interval. We don't care about the specific IDs contained in it; the question is about the number of IDs included. Therefore, our job is simply to add up all the lengths of the intervals using the formula ``length = end - start + 1`` to get our answer.