# Introduction To Generics In Java

When using Java, we often write classes and algorithms that work around certain data types. Let's look at the following `class` as an example:

```
public class StringBox {
    public String myString;
}
```

In the example above, we have a `StringBox` class which represents a real-world box of words. This class's methods perform all of its computation
with regards to the `String myString` field, but what if we wanted a box of `int`s? We would create a new class:

```
public class IntegerBox {
    public int myInt;
}
```

The example above meets our requirements, but as the program grows and we need more types of boxes, it will become unmanageable. We can solve this problem
by using **generics**.

Generics, as the name implies, allows us to create generic classes and algorithms by specifying a type parameter. We can make `StringBox` and `IntegerBox`
into a generic `Box` class as follows:

```
public class Box<T> {
    private T data;
}
```

In the above example, we have created a generic `Box` class with a type parameter `T` and all class methods performing their computation around the `T` type
parameter. We can now specify we want a `String`, `Integer`, or any other type `Box` by specifying a type argument.