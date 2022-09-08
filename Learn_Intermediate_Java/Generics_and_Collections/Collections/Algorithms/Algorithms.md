# Algorithms

The collection framework provides the `Collections` class that has many `static` methods that perform operations such as sorting, finding the maximum or minimum values, and many other operations. Note that `Collections` is different to `Collection`: `Collection` refers to the different data structures such as `LinkedList` and `PriorityQueue`, whereas `Collections` refers to the methods that represent various algorithms such as `binarySearch()` and `sort()`.

To name a few methods provided by the `Collections` class, we have:

* `binarySearch()` - performs a binary search over a `List` to find the specified object and returns the index if found. This method is also overloaded to accept a `Comparator` in order to define a custom sorting algorithm.
* `max()` - finds and returns the maximum element in the `Collection`. This method is overloaded to accept a `Comparator` in order to define a custom sorting algorithm.
* `min()` - finds and returns the minimum element in the `Collection`. This method is overloaded to accept a `Comparator` in order to define a custom sorting algorithm.
* `reverse()` - reverses the order of elements in the `List` passed as an argument.
* `sort()` - sorts the `List` passed as an argument. This method is overloaded to accept a `Comparator` in order to define a custom sorting algorithm.

An example of using some of these `Collections` methods can be found in the code file in this folder.