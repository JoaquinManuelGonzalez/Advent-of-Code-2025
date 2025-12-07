# Logic of Resolution

## Part One

As we are working within a fixed range from ``0`` to ``99``, any addition or subtraction can be solved using the following formula: ``result = (current_value + change) % 100``.

This means that if we go over ``99``, we start again from ``0``, and if we go below ``0``, we go back to ``99``.

## Part Two

Now, instead of thinking about positional movements, let's abstract ourselves a little and think about **the number of complete turns of size ``100`` that we make**.

Based on this idea, we can see that each turn involves passing through ``0`` once, but there is one more thing to consider: we will not always make an exact number of turns; there will be times when we have a **remainder** of movements to make, and in that remainder we also have to see if we pass through ``0``.