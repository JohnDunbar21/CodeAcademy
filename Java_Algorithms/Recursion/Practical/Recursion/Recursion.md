# Recursion

**Recursion** is a computational approach where a method calls itself from within its body, performing the same action multiple times in a row until it reaches a predefined stopping point, also known as a **base case**.

Let’s think about this in the context of our factorial example. Below is the beginnings of a recursive implementation of factorial:

```
	public static int recursiveFactorial(int n) {
		if (n > 0) {
			System.out.println("Execution context: " + n);

			recursiveFactorial(n - 1);
		}

		return 0;
	}
```

Within the `recursiveFactorial()` method, we check whether a condition is met. If it is, then we print the value of `n` and return a call to `recursiveFactorial(n - 1)`. If the condition is not met, we return `0`.

We want a condition that stops being true after n is less than 1, so we want a base case condition of `n > 0` or `n >= 1`.

The code for a RECURSIVE solution to the factorial function can be found in the code file in this folder.