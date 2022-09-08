# Queue

A `Queue` accesses elements in a (usually) First-In-First-Out (FIFO) manner where elements are inserted at the **tail** (back) of the collection and removed from the **head** (front).

A `Queue` has two types of access methods for inserting, removing, and getting the head of the `Queue`.

The following methods throw an exception when:

* `add()` - there is no space for the element.
* `remove()` - there are no elements to remove.
* `element()` - there are no elements to get.

The following methods `return` a special value:

* `offer()` - `false` if there is no space for the element.
* `poll()` - `null` if there are no elements to remove.
* `peek()` - `null` if there are no elements to get.

The methods that return a special value should be used when working with a statically sized `Queue` and the exception throwing methods when using a dynamic `Queue`.

Like the other collection framework interfaces, `Queue` has many implementation. We will look at `LinkedList` and `PriorityQueue`.

We have seen `LinkedList` be used as a `List` implementation, and it is also perfect when needing a basic `Queue` implementation. The `PriorityQueue` ensures the top element is the smallest relative to the data type's natural ordering (or some custom comparison algorithm you provide).

Below is an example of a `Queue` with a `LinkedList` implementation:

```
Queue<String> stringQueue = new LinkedList<>();

stringQueue.add("Mike"); // true - state of queue -> "Mike"
stringQueue.offer("Jeff"); // true - state of queue -> "Mike", "Jeff" 
 
String a = stringQueue.remove() // Returns "Mike" - state of queue -> 1
String b = stringQueue.poll() // Returns "Jeff" - state of queue -> empty
String c = stringQueue.peek() // Returns null
String d = stringQueue.element() // Throws NoSuchElementException
```

In the above example we:

* Created a new `String Queue` reference with a `LinkedList` implementation.
* Called `add()` and `offer()` to insert elements into the `Queue`. Note the state of the `Queue` after each call.
* Called `remove()` and `poll()` to remove and retrieve the element at the front of the `Queue`.
* Called `peek()` and `element()` to retrieve but not remove the element at the front of the `Queue`. Note the results when `stringQueue` is empty.

We can iterate through a `Queue` using the enhanced `for-loop`. For example:

```
// Assuming `stringQueue` has elements -> "Mike", "Jack", "John"
for (String name: stringQueue) {
  System.out.println(name);
}
// OUTPUT TERMINAL: "Mike", "Jack", "John"
```

One thing to note about a `PriorityQueue` is that an enhanced `for-loop` (or `Iterator`) makes no guarantee that the elements will be ordered after the head element.

An example of creating a `Queue` and iterating through it can be found in the code file in this folder.