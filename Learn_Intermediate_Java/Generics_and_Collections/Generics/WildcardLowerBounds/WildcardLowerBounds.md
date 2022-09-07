# Wildcard Lower Bounds

While generic code can have an upper bound when defined using a type parameter or wildcard, we can also provide a **lower bound**. A lower bound wildcard restricts the wildcard to a class or interface and any of its parent types. For example:

```
public class Util {
    public static void getBag(Bag<? super Integer> bag) {
        return bag;
    }
}
```

In the example above we used the `super` keyword to restrict the argument to `getBag()` to be a `Bag` of `Integer`, `Number`, or `Object`. If a call to `getBag()` with `Bag<Double>` was made, it would result in an exception as `Double` is not an `Integer` or one of its parents.

Some important things to note about lower bounds are:

* They cannot be used with generic type parameters, only wildcards.
* A wildcard cannot have both a lower and upper bound, in this case, it is best to use a type parameter.

There are some general guidelines provided by Java as to when you should use what type of wildcard:

* An upper bound wildcard should be used when the variable is being used to serve some type of data to the code.
* A lower bound wildcard should be used when the variable is receiving data and holding it to be used later.
* When a variable that serves data is used and only uses `Object` methods, an unbounded wildcard is preferable.
* When a variable needs to serve data and store data for use later, a wildcard should not be used (use a type parameter).

An example of adding lower bounds to generic code can be found in the code files in this folder.