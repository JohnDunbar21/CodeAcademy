# Iteration with Recursion

### Learning how to iterate through data structures using recursive methods.

Using loops and element indices, we have been able to access each element in a `String`, array, or `ArrayList` in order to gather information about the data each structure contained. Iteration isn’t the only way to access individual elements of a data structure; we also have the ability to parse through data via recursion.

## Iteration with Loops

Take a look at the method `reverseString()` below that takes in a `String` as a parameter and returns a `String` with the characters reversed:

```
public static String reverseString(String text) {
  String reversed = new String("");
  for (int i=0; i < text.length(); i++){
    reversed = text.charAt(i) + reversed;
  }
  return reversed;
}
 
public static void main(String[] args) {
  String str = new String("howdy");
  String reverse = reverseString(str);
  System.out.println(reverse); // Prints: ydwoh
}
```

We use a loop to iterate through the length of our `String` parameter. To access an individual element, we select the element with an index value that equals the current value of our loop control variable `i`.

## Iteration with Recursion

We can recreate this method using recursion:

```
public static String reverseString(String text){
  // base case
  if (text.length() == 0) {
    return text;
  } else {
    // recursive call
    return reverseString(text.substring(1)) + text.charAt(0);
  }
}
 
public static void main(String[] args) {
  String str = new String("howdy");
  // calling recursive function
  String reverse = reverseString(str);
  System.out.println(reverse); // Prints: ydwoh
}
```

Let’s go over this version of `reverseString()`. As a reminder, a recursive method calls itself over and over again until a condition, or base case, is met. In `reverseString()`, the base case is met when the parameter `String` value, `text`, has a length of `0`.

While the base case is not met, we must call the method again. Every time we recursively call a method, we send a new argument value as a parameter. In this example, our argument value is a substring that contains the value of our original `String` with the first element of the `String` removed. For example, in the first call to `reverseString()` which occurred in the `main()` method, the value of text was "howdy". In the first recursive call, the argument value was `reverseString(text.substring(1))`, which equaled "owdy". In the second recursive call, the argument value became "wdy". This continues until we send "" as an argument and the base case is met.

One of the tricky parts of recursion is that we end up with many different local variables of the same name. On the first recursive call, "howdy" is being stored in the variable named `text`. When we make the next recursive call, that recursive call has its own local `text` variable that contains "owdy". Each recursive call has its own set of local variables.

The parameter value in a recursive call is important because it keeps track of the recursive process. We use the parameter value from our recursive calls in the same way we used the loop control variable in the previous version of `reverseString()`. In the first version of `reverseString()` we’d use `text.charAt(i)` to select the current element value of the String and then prepend it to reverse. In the second version of `reverseString()` we use a recursive call to select the current element value of the `String` and then prepend it to the element at index `0` of the `String`.

```
public static int getTotal(ArrayList<Integer> arr) {
  int sum = 0;
  for (int i = 0; i < arr.size(); i++) {
    sum += arr.get(i);
  }
  return sum;
}
 
public static void main(String[] args) {
  ArrayList<Integer> myArray = new ArrayList<Integer>();
  myArray.add(3);
  myArray.add(5);
  myArray.add(6);
  myArray.add(9);
 
  int total = getTotal(myArray);
  System.out.println(total); // Prints: 23
}
```

Above you’ll see an iterative method that adds up the numbers in an ArrayList. To rewrite this with recursion, we’d need to do the following.

* Create a base case that returns `0` when the `ArrayList` has a size of `0`.
* Otherwise, return the sum of the first element + recursive call to `getTotal()` with the `ArrayList` value minus the first element as the argument.

```
import java.util.ArrayList;
class Total {

  public static int getTotal(ArrayList<Integer> arr) {
    // Base Case
    if (arr.size() == 0) {
      return 0;
    } else {
      int temp = arr.get(0);
      arr.remove(0);
      return temp + getTotal(arr);
    }
  }

  public static void main(String[] args) {
    ArrayList<Integer> myArrayLs = new ArrayList<Integer>();
    myArrayLs.add(3);
    myArrayLs.add(5);
    myArrayLs.add(6);
    myArrayLs.add(9);
  
    int total = getTotal(myArrayLs);
    System.out.println(total);
  }
}
```