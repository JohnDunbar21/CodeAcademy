# Multiple Type Parameters

What if our program needs to specify two or more parameter types? Let's look at an example below:

```
public class Box<T, S> {
    private T item1;
    private S item2;
    
    // below would be constructors, getters, and setters
}

Box<String, Integer> wordAndIntegerBox = new Box<>("Hello", 5);
```

In the example above we have created a generic `class Box` with two type parameters, `T` and `S` by using a comma-separated list of type parameters in the diamond operator. We also instantiate a `Box` reference named `wordAndIntegerBox` by providing the necessary type arguments in a comma-separated list, `<String, Integer>`.

This can also be done for interfaces and methods. Let's look at the example below for how to do so for a method:

```
public class Util {
    public static <T, S> boolean areNumbers(T item1, S item2) {
        return item1 instanceof Number && item2 instanceof Number;
    }
}

boolean areNums = Util.areNumbers("Hello", 34); // Returns false
```

In the example above we created a `static` `areNumber()` method that has two type parameters, `T` and `S`. Note that a comma-separated list of type parameters, `<T, S>`, must be specified in the method signature prior to the return type. If it wasnt for the JVM type interference, the code above would been called as:

`Boolean areNums = Util.<String, Integer>areNumbers("Hello", 34); // Returns false`

In the elaboration above we explicitly specified the type arguments `<String, Integer>` before the method name. Type inferences will infer these types from the arguments passed in, `"Hello"` and `34`, making the explicit arguments unnecessary.

An example of using a multiple-type parameter class can be found in the code files in this folder.