# Interfaces

We've seen how to create a generic `class` but we can also create a generic `interface`. Let's look at an example:

```
public interface Replacer<T> {
    void replace(T data);
}
```

The generic `interface Messenger` is created similarly to a generic `class` where the type parameter `<T>` must be
specified after the `interface` name. Interface method declarations are similar to non-generic interfaces and can
be used as the argument to the `interface` type parameter. For example, let's have our `Box` generic `class`
implement the `interface Replacer`:

```
public class Box <T> implements Replacer<T> {
    private T data;

    @ Override
    void replace(T data) {
        this.data = data;
    }
}
```

In the example above, the `Box` type parameter `<T>` will be used as the type argument for the `Replacer` type parameter
`<T>`.

We can also have a non-generic `class` implement a generic interface by specifying the type argument to the `interface`.
For example:

```
public class StringBag implements Replacer<String> {
    private String data;

    @ Override
    void replace(String data) {
        this.data = data;
    }
}
```

In the above example, the `StringBag` is a non-generic `class` that implements `Replacer` and provides `<String>` as the
argument to the type parameter. Notice that the `replace()` parameter `data` has a `String` type as opposed to the 
generic `T` in the previous example.

Now, let's create `interface` type references similarly to how we created generic `class` references:

```
Replacer<Integer> boxReplacer = new Box<>(); // Using generic 'Box'
Replacer<String> bagReplacer = new StringBag(); // Using non-generic 'StringBag' implementation
```

In the above example we created two `Replacer` references. The `Box` implementation can be of any type, but the `StringBag`
implementation needs to be a `<String>` because of the non-generic class implementation.

Examples of using generic interfaces and references can be found in the code files in this folder.