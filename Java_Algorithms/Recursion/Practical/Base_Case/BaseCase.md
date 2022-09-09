# Base Case

Despite returning a call to `n * recursiveFacorial(n - 1)`, the solution to the last exercise did not change the output:

```
Execution context: 4
Execution context: 3
Execution context: 2
Execution context: 1
0
```

Why is the returned value not equal to the product of n in each execution context? We didn’t define a base case. To understand the need for a base case, it’s worth discussing the call stack that Java creates when you call `recursiveFactorial()`.

If you called:

`recursiveSolution = recursiveFactorial(3)`

Java would create a call stack with the following events:

1. `recursiveFactorial(3)` = `3 * recursiveFactorial(2)`
2. `recursiveFactorial(2)` = `2 * recursiveFactorial(1)`
3. `recursiveFactorial(1)` = `1 * recursiveFactorial(0)`

The return value associated with each method call depends on the value returned by the `n - 1` context.

Because our current implementation returns `0` when `n` is zero, each product in the above call-stack, starting with event 3, will be multiplied by `0`. This leads to a `0` solution for each of the contexts above it.

We can fix this with a base case. When the base case is met (n == 0), the factorial method should return a number.

An exmaple of the base case being implemented can be found in the code file in this folder.