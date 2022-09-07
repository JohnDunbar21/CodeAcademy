# Wrapper Classes

Generics allow our programs to adapt to different data type needs, but one issue with them is that we cannot use primitive types
(`int`, `double`, `boolean`, etc) as arguments to generic type parameters. For example, we cannot create a `Box` of integers this way:

`Box<int> intBox = new Box<>(56);`

Fortunately, Java provides **wrapper classes** to allow us to create objects of primitive types and use them as type parameters. We
can now create a `Box` of integers this way:

`Box<Integer> intBox = new Box<>(56);`

In the example above, the `Integer` wrapper class is used in place of `int` to work as a type argument. Also, notice that we are able
to pass `56` as the argument to the constructor and this is because of **autoboxing**.

Autoboxing allows wrapper classes to take primitive values and convert them to their corresponding wrapper object by automatically
calling the `valueOf()` method. For example, the following statements are equivalent when creating a `Box<Integer>`:

```
Integer a = 56; // Autoboxing, automatic call to 'valueOf()'
Box<Integer> intBox1 = new Box<>(a);
Box<Integer> intBox2 = new Box<>(56); // Autoboxing, automatic call to 'valueOf()'
Box<Integer> intBox3 = new Box<>(Integer.valueOf(56));
```

We can also take the wrapper object and convert it back to its primitive value using one of the wrapper object's `Value()` methods. This
process is also automated for us and is known as **unboxing**. For example:

```
Integer a = 56;
int aPrimitive1 = a.intValue(); // Return primitive 'int' value from 'Integer' object
int aPrimitive2 = a; // Unboxing, automatic call to 'intValue()'
```

| Primitive Data Types | Wrapper Classes |
|:--------------------:|:---------------:|
| int                  | Integer         |
| short                | Short           |
| long                 | Long            |
| byte                 | Byte            |
| float                | Float           |
| double               | Double          |
| char                 | Character       |
| boolean              | Boolean         |