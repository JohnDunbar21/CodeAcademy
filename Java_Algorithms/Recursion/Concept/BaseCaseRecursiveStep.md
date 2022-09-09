# Base Case and Recursive Step

Recursion has two fundamental aspects: the base case and the recursive step.

When using iteration, we rely on a counting variable and a boolean condition. For example, when iterating through the values in a list, we would increment the counting variable until it exceeded the length of the dataset.

Recursive functions have a similar concept to iterative functions, where the break condition is called the base case. The base case dictates whether the function will recurse, or call itself. Without a base case, it’s the iterative equivalent to writing an infinite loop.

Because we are using a call stack to track the function calls, your computer will throw an error due to a **stack overflow** if the base case is not sufficient.

The other fundamental aspect of a recursive function is the recursive step. This portion of the function is the step that moves us closer to the base case. In an iterative function, this is handled by a loop construct that decrements or increments a counting variable which moves the counter closer to a boolean condition, terminating the loop.

In a recursive function, the “counting variable” equivalent is the **argument to the recursive call**. If we’re counting down to 0, for example, our base case would be the function call that receives `0` as an argument. We might design a recursive step that takes the argument passed in, decrements it by one, and calls the function again with the decremented argument. In this way, we would be moving towards `0` as our base case.

Analyzing the Big O runtime of a recursive function is very similar to analyzing an iterative function. Substitute iterations of a loop with recursive calls.

For example, if we loop through once for each element printing the value, we have a `O(N)` or **linear runtime**. Similarly, if we have a single recursive call for each element in the original function call, we have a `O(N)` or **linear runtime**.