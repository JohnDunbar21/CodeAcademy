# Collection

The `Collection` interface provides a generic, general purpose API when our program needs a collection of elements, and doesn't care about what type of collection it is.

Implementing classes may implement collections methods and restrict them, like a `Set` does to only contain unique elements. Implementing classes, or extending interfaces, does not need to implement all methods and instead will throw an `UnsupportOperationException` when a `Collection` method is not implemented.

The `add()` and `remove()` methods are in the `Collection` interface, but some additional methods are:

* `addAll()` - recieves a `Collection` argument and adds all the elements.
* `isEmpty()` - returns true if the collection is empty, and `false` otherwise.
* `iterator()` - returns an `Iterator` over the collection.
* `size()` - returns the number of elements in the collection.
* `stream()` - returns a `Stream` over the elements in the collection.
* `toArray()` - returns an array with all elements in the collection.

Below is an example of how some of these methods are used:

```
Collection<Integer> collection = new ArrayList<>();

collection.add(4);
collection.add(8);
 
boolean isEmpty = collection.isEmpty(); // false
int collectionSize = collection.size(); // 2
 
Integer[] collectionArray = collection.toArray(new Integer[0]);
```

In the above example we:

* Created an `Integer Collection` with an `ArrayList` implementation.
* Called `add()` to add elements to the end of the `Collection`.
* Called `isEmpty()` to check if `collection` has elements.
* Called `size()` to get the number of elements in `collection`.
* Called `toArray()` to transform `collection` to an array. Note that the `new Integer[0]` argument specifies the type of array we want returned.

We can iterate through a `Collection` with an enhanced `for-loop` as seen in other folders in this section.

An example of working with a `Collection` can be found in the code file in this folder.