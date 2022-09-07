# Methods

What can we do if we simply want one of our methods to be generic and not the whole `class` or `interface`? We can create 
generic methods to do just that, for example:

```
public class StringBox {
    private String data;

    public <T> boolean isString(T item) {
        return item instanceof String;
    }
}

StringBox box = new StringBox();
box.isString(5); // Returns false
```

In the example above, using the `class StringBox`, we created the generic method `isString()` with a generic type `T` as a 
method parameter. It is important to note that generic methods need to include the type parameter, `<T>` in our example, 
prior to the return type, even if the return type is `void`. The generic method is called like any other method as shown.

We can also do thyis with `static` methods and their signatures have the same requirements except for also needing the 
`static` keyword. For example:

```
public class StringBox {
    private String data;

    public static <T> boolean isString(T item) {
        return item instanceof String;
    }
}

StringBox.isString(5); // Returns false
```

In the above example, we see how we made the `isString()` a `static` method by simply adding `static` to the method signature.
We call it by using the `class` name instead of an object.

An example of creating generic methods can be found in the code file in this folder.