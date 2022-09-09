# Recursion Outline

Recursion is a strategy for solving problems by defining the problem in terms of itself. For example, to **sum the elements of a list** we would take the first element and add it to the **sum of the remaining elements**.

How would we get that sum of remaining elements though? We take the first element of the remaining elements and add it to the sum of the remaining elements.

In programming, recursion means a function definition will include an invocation of the function **within its own body**. Here’s a pseudo-code example:

```
define function, speller
  if there are no more letters
    print "all done"
  print the first letter
  invoke speller with the given name minus the first letter
```

If we invoked this function with “Joe” as the argument, we would see “J”, “o”, and “e” printed out before “all done”.

We called the function a total of 4 times:

1. function called with "Joe".
2. function called with "oe".
3. function called with "e".
4. function called with "".

Let us deconstruct this pseudocode so we can better understand it.

```
if there are no more letters
    print "all done"
```

The above is referred to as the **base case**. We are NOT invoking the function under this condition.

`print the first letter`

The above section solves **a piece** of the problem. If we want to spell someone's name, we will have to spell **at least** one letter.

`invoke speller with the given name minus the first letter`

The above section is the **recursive** step, calling the function with the arguments which bring us closer to the base case: in this example, we are reducing the length of the name by a single letter. Eventually there will be a function call with no letters given as the argument.

Below is pseudocode for an iterative approach to the same problem for comparison:

```
define function, speller
  for each letter in the name argument
    print the letter
  print "all done"
```