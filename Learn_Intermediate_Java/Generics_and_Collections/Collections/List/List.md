# List

The collection framework provides a core set of interfaces to define different collection behaviours, one of the core interfaces being the `List` interface. A `List` is a collection where its elements are ordered in a sequence. `List`s allow us to have duplicate elements and complete control over where elements are inserted in the sequence. Like arrays, the postition of a `list` is known as the **index** and is `0` based. Unlike arrays, which have a static size, `List`s are dynamically sized.

We will be focussing on `ArrayList` and `LinkedList` for now. The `ArrayList` is the preferred implementation for most use cases, but the `LinkedList` performs better than an `ArrayList` if your program mostly inserts and deletes elements.

Below is an example of creating a `List` using an `ArrayList` as its implementation:

```
List<Integer> intList = new ArrayList<>(); // Generates an empty List
intList.add(4); // 4
intList.add(6); // 4, 6
intList.add(3); // 4, 6, 3
intList.set(1, 3); // 4, 3, 3

int a = intList.get(2); // a = 3
int b = intList.indexOf(3); // b = 1

List<Integer> subIntList = intList.subList(1, 3); // subIntList -> 3, 3
```

In the above example we:

* Created a `List` reference named `intList` with an `ArrayList` implementation.
* Called `add()`, which appends elements to the end of the `List`. We can see the state of `intList` after each call in the comments.
* Called `intList.set(1,3)`, which replaces the element at index `1` with `3`.
* Called `get()`, which gets the value at index `2`.
* Called `indexOf()`, which returns the index of the first occurrence of `3` (the first `3` is at index `1`).
* Called `subList()`, which returns a sublist in a new `List` with the elements specified by the starting index `1` (inclusive) and ending at index `3` (exclusive).

We can iterate throgh a `List` using the enhanced `for-loop`. For example:

```
// Assuming intList has elements -> 1, 5, 2, 6, 1
for (Integer number: intList) {
    System.out.println(number);
}
// OUTPUT TERMINAL: 1 5 2 6 1
```

In the above example we used the enhanced `for-loop` which iterates through the elements in `intList` from index `0` to the end of the list. Note that we use the `int` wrapper class `Integer` to iterate through the elements in `intList`.

Code examples of implementing a List and iterating through it can be found in the code file in this folder.