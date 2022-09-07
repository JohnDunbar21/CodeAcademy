# Classes

Previously we saw how generics can help make our code more manageable and flexibile to future needs. We created the following generic class:

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
```

In the example above, notice that:

* The type parameter must be specified within the diamond operator(`<>`) after the `class` name.
* The type parameter, `T`, is similar to a method parameter but instead receives a `class` or `interface` type as an argument as opposed to reference or primitive type.
* The constructor has a `T` type parameter when wanting to alter `data`.
* The getter returns the type parameter `T` when returning `data`.

Creating generic classes is great, but we also need to be able to create references to them in our programs:

`Box<String> myStringBox = new Box<>("Apple);`

In the example above, we can see the reference `myStringBox` is created similarly to non-generic references but differ in:

* Needing the diamond operator with the `class` or `interface` type argument, `<String>` in this example, after the `class` name.
* Needing the empty diamond operator prior to calling the constructor, `new Box<>("Apple)`.

When defining type parameters, although not being a hard requirement, it's best practice to make them single, uppercase letters to easily distinguish them from the names of classes
or variables. By convention, common type parameters include `E` (Elements), `K` (Key), `N` (Number), `T` (Type), `V` (Value), and `S` (or `U` or `V`) for multiple type parameters.

One final thing to note is that prior to Java 7, generic references needed to be created like:

`Box<String> myStringBox = new Box<String>("Apple");`

In the example above, the `<String>` type argument also needed to be specified prior to calling the constructor. This is no longer necessary due to Java's **type inference** where the
compiler can infer the `<String>` type argument in the constructor from the context of the reference definition `Box<String>`.

Examples of creating a generic class and creating an instance of it can be found in the Container.java, Main.java, and Book.java files of this folder.