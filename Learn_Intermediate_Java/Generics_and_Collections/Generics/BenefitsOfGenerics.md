# Benefits of Using Generics in Java

Let's discuss some benefits of using generics besides making our code more scalable. We can actually get away with not providing a type argument to a generic `class` or `interface`, this is known as using a **raw type** and they were prevalent prior to the introduction of generics in Java 5. For example:

```
public class Box <T> {
    private T data;

    public Box(T data) {
        this.data = data;
    }

    public T getData() {
        return this.data;
    }
}

Box box = new Box<>("My String"); // Raw type box
String s2 = (String) box.getData(); // No incompatible type error
String s1 = box.getData(); // Incompatible type error
```

In the example above:

* Using the generics class `Box`, we have created a raw type `Box` and passed `"My String"` as an assignment.
* We called `getData()` again and typecast the result in `String s2`. This has no error because we are explicitly down casting to `String`.
* We call `getData()` and store the result in `String s1`. We get an `Incompatible type` error as `getData()` returns an `Object` type and we are trying to implicitly downcast to a `String`.

Raw types should be avoided because generics:

* Avoid `Incompatible type` errors when retrieving data from raw types.
* Avoid a potential runtime `ClassCastException` when explicitly typecasting.
* Give us compile-time type checking, which helps detect bugs before our code runs.
* Help when the JVM applies **type erasure**.

When using generics, type erasure is applied by the JVM and will cause all type parameters to be replaced by `Object` or their type bounds. The type erasure will also apply any necessary type casting to ensure our code is type-safe and ensure that the final byte code produced has non-generic types.