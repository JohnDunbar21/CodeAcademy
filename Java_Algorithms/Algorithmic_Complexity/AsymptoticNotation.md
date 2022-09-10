# Asymptotic Notation

## TLDR

* We use asymptotic notation to describe the runtime of a program: the three types are big Theta, big Omega, and big O.
* We use big Theta, $\Theta$, to describe the runtime if the runtime of the program is the same in every possible case.
* The different common runtimes from fastest to slowest are: $\Theta(1)$, $\Theta(\log N)$, $\Theta(N)$, $\Theta(N*\log N)$, $\Theta(N^2)$, $\Theta(2^N)$, and $\Theta(N!)$.
* We use big Omega, $\Omega$, to describe the best case runtime of a program.
* We use big O, $O$, to describe the worst case runtime of a program.
* **Generally, a program's runtime is expressed in terms of big O**.
* When finding the runtime of multiple steps, you can divide the program into different sections and add the runtimes of the various sections, then take the slowest runtime and use it to describe the entire program.
* When analysing the runtime of a program, we mainly care about the part of the program that is the slowest.

### Why Asymptotic Notation?

When writing programs, we as programmers need to make smart choices to ensure that our code runs smoothly. Computers themselves appear to not evaluate programs, but when scaling programs to deal with large quantities of data, writing efficient code becomes the difference between its success and failure. In the computer science field, the efficiency of a program is referred to as its **runtime**.

Timing the program would be futile as different machines run at different speeds, and programming is done in many different languages, so we require a general way to define a program's runtime across the variable factors: this is **Asymptotic Notation**.

With asymptotic notation, we define the program's runtime by looking at how many instructions the machine has to perform based on the size of the input: for example, if we were to calculate the maximum element in a collection, we would need to examine each element in the collection. That examining step is the same regardless of the language used, or the machine's abilities. In asymptotic notation, we refer to the size of the inputs as `N`. We may be looking through a collection of 10 or 100 elements, but we only need to know how many steps are performed **relative to the input** so `N` is used in place of a specific number (if there is a second input, we define the size of it as `M`).

There are varieties of asymptotic notation that focus on different concerns.

Some will communicate the **best case** scenario for a program: for example, if we were searching for a value within a collection, the best case would be if we found the element in the first place we looked. Another type will focus on the **worst case** scenario, such as if we searched for a value, looked in the entire dataset and did not find it. Typically we focus on the worst case scenario so there is an upper bound of runtime to communicate: a way of saying "things may get this bad, or slow, but they will not get any worse".

### What is Asymptotic Notation?

Instead of timing a program using seconds, we can calculate the runtime using asymptotic notation by looking at how many operations the machine has to perform relative to the input `N`.

For example, a program that has an input of size `N` may tell the computer to run $5N^2+3N+2$ instructions (this expression is purely for demonstration purposes). This is clearly a very messy expression, but with asymptotic notation, we **drop all of our constants** (the numbers) because as `N` becomes larger, the numerical constants will make only minor differences.

 After dropping our constants, we are left with $N^2+N$, but if we take each of these terms out and graph them, we can see that $N^2$ grows far quicker than $N$.

<img title="" alt="" src="https://content.codecademy.com/programs/cs-path/asymptotic%20notation/conceptual/runtimes%20compare.png">

For example, when `N` is 1000:

* The $N^2$ term is 1,000,000.
* The $N$ term is 1,000.

It is clear from the graph above that $N^2$ would have a longer runtime than $N$, and when `N` becomes larger than 1,000, the difference becomes even more noticable. As the difference between the two is so massive in this example, we do not need to consider the $N$ term when calculating the runtime: therefore the runtime of the example expression is $N^2$.

There are three different ways to describe the runtime: big Theta or $\Theta(N^2)$, big O or $O(N^2)$, big Omega or $\Omega(N^2)$. The details between the three notations will be explained further in the document.

You may see the term **execution count** being used in evaluating algorithms, this is because execution count is more precise than Big O notation. The following Java method, `addUpTo()`, can be as low as $2N$ or as high as $5N+2$, depending on how we count the number of operations:

```java
public class Main() { 
  void int addUpTo(int n) {
    int total = 0;
    for (int i = 1; i <= n; i++) {
      total += i;
    }
  return total;
  } 
}
```

Big O Notation is a way to formalise 'fuzzy counting', and allows us to talk formally about the runtime of an algorithm as the input(s) grow.

### Big Theta

We use big Theta when a program has only **one case** in term of runtime. Take a look at the pseudocode for a function that prints the values in a list below:

```
Function with input that is a list of size N:
    For each value in list:
        Print the value
```

The number of instructions the machine has to perform is based on how many iterations the loop will do because if the loop does more iterations, then the computer will perform instructions. Below is a table that shows how many iterations the loop will do dependening on the value of `N`:

| Size of List | Number of Iterations |
|:------------:|:--------------------:|
| 1            | 1                    |
| 2            | 2                    |
| 3            | 3                    |
| .            | .                    |
| .            | .                    |
| .            | .                    |
| .            | .                    |
| .            | .                    |
| N            | N                    |

As the table shows, with a list of size `N`, the program has a linear runtime of `N` as the program has to print a value `N` times. Thus we would say the runtime is $\Theta(N)$.

Below is a more complicated example where the pseudocode takes in an integer `N` and counts the number of times it takes for `N` to be divided by 2 until `N` reaches 1.

```
Function that has integer input N:
    Set a count variable to 0
    Loop while N is not equal to 1:
        Increment count
        N = N/2
    Return count
```

Let's see how many iterations the loop will perform based on the input `N`:

| N     | Number of Iterations |
|:-----:|:--------------------:|
| 1     | 0                    |
| 2     | 1                    |
| 4     | 2                    |
| 8     | 3                    |
| 16    | 4                    |
| .     | .                    |
| N     | $\log_2(N)$          |

As this table shows, in every input case, the loop will iterate $\log_2(N)$ times. However, we drop all constants in asymptotic notation, so the runtime of this specific code would be $\Theta(\log N)$.

### Common Runtimes

Below is a list of the most common runtimes that runs from fastest to slowest:

* $\Theta(1)$ - This is a **constant** runtime. This is the runtime when a program will always do the same thing regardless of the input. For example, a program that only prints “hello, world” runs in $\Theta(1)$ because the program will always just print “hello, world”.
* $\Theta(\log N)$ - This is a **logarithmic** runtime. You often see this runtime in search algorithms.
* $\Theta(N)$ - This is a **linear** runtime. You often see this runtime when you have to iterate through an entire dataset.
* $\Theta(N*\log N)$ - You often see this runtime in sorting algorithms.
* $\Theta(N^2)$ - This is a **polynomial** runtime. You will often see this when you have to search through a two-dimensional dataset (such as a matrix) or nested loops.
* $\Theta(2^N)$ - This is an **exponential** runtime. You often see this in recursive algorithms.
* $\Theta(N!)$ - This is a **factorial** runtime. You will see this runtim when you have to generate all of the different permutations of something. For example, a program that generates all the different ways to order the letters "abcd" would have this runtime.

<img title="" alt="" src="https://content.codecademy.com/programs/cs-path/asymptotic%20notation/conceptual/commonRuntimes.svg">

### Big Omega and Big O

A program can have different runtimes for the best and worst case scenarios. For example, a program could have a best case runtime of $\Theta(1)$ and a worst case runtime of $\Theta(N)$. We use different notation when this is the case, where big Omega or $\Omega$ is used to describe the best case and big O or $O$ to describe the worst case. Below is some pseudocode that will return `true` if 12 is in the list and `false` otherwise.

```
Function with input that is a list of size N:
    For each value in the list:
        If value is equal to 12:
            Return True
    Return False
```

How many times will the loop iterate? Let’s take a list of size 1000: if the first value in the list was 12, then the loop would only iterate once. However, if 12 wasn’t in the list at all, the loop would iterate 1000 times. If the input was a list of size `N`, the loop could iterate anywhere from 1 to `N` times depending on where 12 is in the list (or if it’s in the list at all). Thus, in the best case, it has a constant runtime and in the worst case it has a linear runtime.

There are many ways to describe the runtime of this program:

* This program has a best case runtime of $\Theta(1)$.
* This program has a worst case runtime of $\Theta(N)$.
* This program has a runtime of $\Omega(1)$.
* This program has a runtime of $O(N)$.

It may be tempting to say that the program has a runtime of $\Theta(N)$, but this is not true as the program does not have a linear runtime in every case (only the worst case).

When describing the runtime, typically it is the worst case scenario being referred to when there are multiple scenarios such as the one discussed above.

### Adding Runtimes

Sometimes a function/program can have multiple scenarios occuring at once: for example, the pseudocode below prints all the positive values up to `N` and then returns the number of times it takes to divide `N` by 2 until `N` is 1.

```
Function that takes a positive integer N:
    Set a variable i equal to 1
    Loop until i is equal to N:
        Print i
        Increment i
 
    Set a count variable to 0
    Loop while N is not equal to 1:
        Increment count
        N = N/2
    Return count
```

We begin by dividing the pseudocode into two distinct chunks:

* In the first loop we iterate until we reach `N`. Therefore the runtime of the first loop is $\Theta(N)$.
* In the second loop, since `N` is being halved on each iteration, the runtime of this second loop is $\Theta(\log N)$.

When we combine these runtimes, we are left with: $\Theta(N)$ + $\Theta(\log N)$. However, when analysing the performance of a program, we only consider the worst case scenario. Therefore, since the first loop runs in a linear fashion and the second loop runs in a logarithmic fashion, the **overall runtime would be $\Theta(N)$**. It would also be appropriate to say that the runtime is $O(N)$ since this represents the worst case scenario, and people will generally use big O notation.