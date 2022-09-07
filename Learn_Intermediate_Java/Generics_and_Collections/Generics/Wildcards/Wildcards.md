# Wildcards

Generic code can take type arguments to help generalise our code, but we can make our code even more general when we don't need the more strict type checking of using type parameters by using **wildcards**. A wildcard, denoted by the `?` symbol, represents an unknown type when used with generic methods. Let's look at an example:

```
public class Util {
    public static void printBag(Bag<?> bag) {
        System.out.println(bag.toString());
    }
}

Bag<String> myBag1 = new Bag("Hello");
Bag<Integer> myBag2 = new Bag(23);
Util.printBag(myBag1); // Prints Hello
Util.printBag(myBag2); // Prints 23
```

In the above example we defined a `static` generic method that works on `Bag` types. We specify that the `Bag`, which is the generic class, can be of any type by using the wildcard, `Bag<?>`. We also created two `Bag` references of different types, `String` and `Integer`, and used them as arguments to `printBag()`.

You may be thinking how this is different than using a type parameter because we could write the above method as:

```
public static <T> void printBag(Bag<T> bag) {
    System.out.println(bag.toString());
}
```

In the above example we have defined the parameter as `Bag<T>` as opposed to `Bag<?>` and in this implementation, this makes no difference, but you may notice that the wildcard version is far simpler. It's simpler in not needing the extra `<T>` before the return type and easier to make sense of when reading the signature.

In general we should use type parameters when we have a relationship between the type of arguments and the return type. For example:

```
public static <T> Bag<T> getBag(Bag<T> bag) {
    return bag;
}
```

In the above example we created a method that accepts a `Bag` of some type `T` and returns a `Bag` of the same type `T`. This use of type parameters maintains strong type checking through our code.

We can also create upper bounds and lower bounds when using wildcards. For example:

```
public static void printBag(Bag<? extends Number> bag) {
    System.out.println(bag.toString());
}
```

In the above example, `printBag()` accepts any `Bag` that is a `Number` and will error-out when passing a type of `Bag` that does not fall into that parent-child hierarchy, for example, a `String Bag`.

An example of wildcards being used in generic code can be found in the code files in this folder.