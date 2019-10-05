# tek5-algo-intro

# Task 1: Snowplow Problem

## Running

Requires numpy installed

```
python3 snowplow/
```

## Why is it polynomial ?

The global algorithm complexity is `n * log(n) + (n ^ 2) * log(n) - n` or `n * (log(n) + n * log(n) - 1)`.

I'll explain the algorithm step by step

### parcours call

- sort using merge sort is `n * log(n)` complexity
- Main Loop is `(n ^ 2) * log(n) - n` complexity

#### Main Loop

The main loop will check that there are houses left to process in the array of houses. As houses are removed by chunks from one side only
(left or right of current position), it can take `2` iterations to empty the array, but it can also take `n` iterations in the worst case.

This loop can run between `2` and `n` times, so we'll consider this loop has a complexity of `n`.
The loop runs the limit check loop every time, so the general complexity if (`n` * `(n - 1) * log(n)` or (`(n ^ 2) * log(n) - n`))

##### Limit Check Loop

The logic behind this loop is to take the remaining houses, create a left and right index (started at the leftmost and rightmost houses),
and bring the indexes closer until one of them crosses the position of the snowplow. Once it's done, we know that we should take the other 
index into account and move from the snowplow to the other index. To move the indexes, we compute a score that determines if it's worth to move
to this point compared to moving to the other point. We always compare left and right and estimate how much time we would lose by going to this point,
averaged to the number of houses crossed.

- Finding the center of the array (index of house closest to snowplow position) takes `log(n)` steps (dichotomic approach).
- The loop can be iterated up to `n-1` times, this worst case scenario happens when the left and right index keep advancing both.

One Limit check loop has a complexity of `(n - 1) * log(n)`


TODO

# Task 2: ?