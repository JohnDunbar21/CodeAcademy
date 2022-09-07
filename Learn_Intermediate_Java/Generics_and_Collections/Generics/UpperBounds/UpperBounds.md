# Upper Bounds

Generics make our code scalable by allowing us to provide type arguments to classes, interfaces, and methods, but what if we needed to restrict what class or interface could be used as a type argument? We can implement this by assigning an **upper bound**. An upper bound will limit the type parameter to a parent type or any of its child types. Let's look at the example below:

```
public class Box <T extends Number> {
    private T data;
}
```

In the example above, we defined a type parameter `T` and added an upper bound type `Number` for `T` with `extends Number`. The `extends` in this example means that `T` can be a `Number` or any of its child classes (or interfaces).

We can create references to `Box` as follows:

```
Box<Integer> intBox = new Box<>(2); // Valid type argument
Box<Double> doubleBox = new Box<>(2.5); // Valid type argument
Box<String> stringBox = new Box<>("Hello"); // Error
```

In the example above, we:

* Created two `Box` references with type arguments `Integer` and `Double`, which are both child classes of `Number`.
* Attempted to create a `Box` reference with type argument `String` and receive an eror because `String` is not a `Number` type or any of its child classes.

We can similarly add upper bounds to generic methods as follows:

```
public static <T extends Number> boolean isZero(T data) {
    return data.equals(0);
}
```

In the example above, it is important to note that we added the `Number` upper bound prior to the return type.

Java also allows us to create a type parameter with multiple bounds. For example:

```
public class Box <T extends Number & Comparable<T>> {
    private T data;
}
```

In the above example, we specify multiple bounds(`Number` and `Comparable`) for type parameter `T` using the `&` operator between the different upper bounds. It is important to note that when defining multiple bounds, any upper bound that is a `class`, in our example `Number`, must come first, followed by any interfaces (in our example `Comparable<T>`).

An example of adding upper bounds to a generic class can be found in the code files in this folder.