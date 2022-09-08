# Map

The `Map` interface does not quite mesh with the hierarchy diagram shown in the Introduction document, but it is an extremely important part of the `Collection` framework.

`Map` defines a generic interface for an object that holds key-value pairs as elements. The **key** is used to retrieve some value, and must be unique, mapping to exactly one value. A `Map` can be thought of as a Java interface for a **Hash Table** data structure. There are many ways to implement `Map`, but we will focus on `HashMap`, `LinkedHashMap`, and `TreeMap` implementations.

The `HashMap` defines no specific ordering for the keys, and is the **most optimised** implementation for retrieving values.

The `LinkedHashMap` keeps the keys in their insertion order, but is slightly less optimised than the `HashMap`.

The `TreeMap` keeps the keys in their natural order (or some custom order defined using a `Comparator`): this implementation has a significant performance decrease when compared to `HashMap` and `LinkedHashMap`. However, `TreeMap` is great when needing to keep a `Collection`'s keys sorted.

A `Map` has the following methods for accessing its elements:

* `put()` - sets the value that the key maps to. Note that this method replaces the value that the key mapped to if the key was already assigned in the `Map`.

* `get()` - gets, but does not remove, the value that the provided key points to (if it exists). This method will return `null` if the key is not in the `Map`.

Below is an example of how to utilise these methods:

```
Map<String, String> myMap = new HashMap<>();
 
myMap.put("Hello", "World") // { "Hello" -> "World" }
myMap.put("Name", "John") //   { "Hello" -> "World" }, { "Name" -> "John" }
 
String result = myMap.get("Hello") // returns "World" 
String noResult = myMap.get("Jack") // return `null`
```

In the above example we:

* Created a `Map` reference that maps a `String` key to a `String` value using the `HashMap` implementation. Note that a `Map` needs a type argument for the key and the value.
* Added key-value pairs to `myMap` using `put()`, where the first argument is the key and the second argument is the value that the key maps to.
* Retrieved the value that the key "Hello" maps to using the `get()` method. The `String` "World" is returned since the key "Hello" exists in the `Map`. The value returned from the key "Jack" is `null` since the key "Jack" does not exist in the `Map`.

We can iterate over a `Map` using an enhanced `for-loop` as shown below:

```
// Given a map, `myMap`, with the following key-value pairs { "Hello" -> "World" }, { "Name" -> "John"}

for (Map.Entry<String, String> pair: myMap.entrySet()){
  System.out.println("key: "+pair.getKey()+", value: "+pair.getValue());
}

// OUTPUT TERMINAL:
// key: Name, value: John
// key: Hello, value: World
```

In the code example above we:

* Called `entrySet()` that returns a `Set` of type `Map.Entry` which represents a key-value pair.
* We define our iterating variable of type `Map.Entry<String, String>` to specify what type of key-value pair we are iterating over.
* Called `getKey()` or `Map.Entry` to get the key of the pair.
* Called `getValue()` of `Map.Entry` to get the value of the pair.

An example of working with a `Map` can be found in the code file in this folder.