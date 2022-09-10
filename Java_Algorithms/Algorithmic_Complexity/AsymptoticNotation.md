# Asymptotic Notation

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