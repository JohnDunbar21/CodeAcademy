# Deque

A `Deque` is a collection that allows us to manipulate elements from both the front and end of the collection.

The `Deque` interface has two types of methods for manipulating the front and back of the collection.

The following methods throw an exception when:

* `addFirst()`, `addLast()` - if there is no space to add an element.
* `removeFirst()`, `removeLast()` - if there is no element to remove.
* `getFirst()`, `getLast()` - if there is no element to get.

The following methods return a special value;

* `offerFirst()`, `offerLast()` - `false` when there is no space to add an element.
* `pollFirst()`, `pollLast()` - `null` when there is no element to remove.
* `peekFirst()`, `peekLast()` - `null` when there is no element to get.

A `Deque` has many implementations, but we will look at the `LinkedList` and `ArrayDeque` implementations. The `LinkedList`, although no the most optimised, is flexible enough to not only be used as a `List` and `Queue` but also as a `Deque`. The `ArrayDeque` is the preferred implementation when needing to manipulate elements at the front and end of a collection.

Below is an example of a `LinkedList` implementation of a `Deque`:

```
Deque<String> stringDeque = new LinkedList<>();

stringDeque.addFirst("A"); // Front -> "A" <- end
stringDeque.offerFirst("B"); // Return `true` - front -> "B", "A" <- end
stringDeque.offerLast("Z"); // Returns `true` - front -> "B", "A", "Z" <- end
 
String a = stringDeque.removeFirst()  // Returns "B" - front -> "A", "Z"
String b = stringDeque.pollLast()  // Returns "Z" - front -> "A" <- back
String c = stringDeque.removeLast()  // Returns "A" - empty deque
String d = stringDeque.peekFirst()  // Returns null
String e = stringDeque.getLast() // Throws NoSuchElementException
```

In the above example above we:

* Called `addFirst()`, `offerFirst()`, and `offerLast()` to add elements. Not that the `offer()` methods return a boolean.
* Called `removeFirst()`, `pollLast()`, and `removeLast()` to remove elements.
* Called `peekFirst()` and `getLast()` to get but not remove the element at the front and back of the `Deque` respectively.

We can iterate a `Deque` from front to back using an enhanced `for-loop` and we can use the `descendingIterator()` method and use the `Iterator` returned to go from back to front.

```
// Assuming `stringDeque` has elements front -> "Mike", "Jack", "John" <- back
Iterator<String> descItr = stringDeque.descendingIterator();
 
while(descItr.hasNext()) {
  System.out.println(descItr.next());
}
// OUTPUT TERMINAL:  "John", "Jack", "Mike"
```

An example of a `Deque` being created and iterating through it can be found in the code file in this folder.