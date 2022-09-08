# Set

A `Set` is a collection of unique elements, and all of its methods ensure this stays true. The collection framework provides different implementations of a `Set` that each have different use cases (below are just a few).

The `HashSet` implementation has the best performance when retrieving or inserting elements, but cannot guarantee any ordering among them.

The `TreeSet` implementation does not perform as well on insertion and deletion of elements, but does keep the elements stored in order based on their values (this can be customised).

The `LinkedHashSet` implementation has a slightly slower performance on insertion and deletion of elements than a `HashSet` but keeps elements in insertion order.

Let's look at a `HashSet` implementation of a `Set`:

```
Set<Integer> intSet = new HashSet<>(); // Empty set

intSet.add(6); // true - 6
intSet.add(0); // true - 0, 6 (no guaranteed ordering)
intSet.add(6); // false - 0, 6 (no change, no guaranteed ordering)

boolean isNineInSet = intSet.contains(9); // Returns false
boolean isZeroInSet = intSet.contains(0); // Returns true
```

In the example above we:

* Created a `Set` reference named `intSet` with a `HashSet` implementation.
* Called `add()`, which adds elements to the `Set` and returns `true` if an element was successfully added, or false if not.
* Called `add()`, noting that the program will not throw an error if we try to insert a non-unique element into the set.
* Called `contains(9)`, which returns `false` because `9` does not exist in `inSet`.
* Called `contains(0)`, which returns `true` because `0` does exist in `intSet`.

We can iterate through a `Set` using the enhanced `for-loop`, but we cannot guarantee that the elements will be ordered when being iterated through. For example:

```
// Assuming intSet has elements -> 1, 5, 9, 0, 23
for (Integer number: intSet) {
    System.out.println(number;)
}
// OUTPUT TERMINAL: 5 0 23 9 1
```

An example of creating a `Set` and iterating through it can be found in the code file in this folder.