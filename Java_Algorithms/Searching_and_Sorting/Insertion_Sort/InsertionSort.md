# Insertion Sort

### Introduction

Insertion sort is a sorting algorithm that creates a final sorted array one item at a time, where on each iteration through an input array, it takes one element and finds the location it belongs in before inserting it.

Much like the selection sort algorithm, the insertion sort works by dividing an input array into two virtual lists: a sorted and unsorted sub-list. Our sorted sub-list initially contains the first element of the input array, and the rest of the elements make up the unsorted sub-list. Insertion sort will go through the unsorted sub-list one by one, removing an element from the unsorted sub-list and then inserting it into the correct position in the sorted sub-list by shifting all the elements in the sorted sub-list that are greater than the element being sorted.

Imagine you have a deck of cards laid out in front of you that you want to sort in ascending order. We focus on the number, not the suit: `{7, 2, 5, 8, -3};`. We can assume the first card, `7`, to be part of the sorted sub-list. Next we will look at the first unsorted element, `2`, and compare it to our sorted element `7`. As `2` is smaller than `7`, we shift `7` one spot to the right in the sorted sub-list and insert `2` before it. We continue this process for each card until we have a final result of `{-3, 2, 5, 7, 8};`

<img title="" alt="" src="https://static-assets.codecademy.com/Paths/ap-computer-science/InsertionSort/insertionSort.png">

### Shift

Two conditions must be met for our code before we make a switch:

1. Is the already sorted item greater than the item we are attempting to sort? If so, shift it to the right, and if not, insert the new card after the already sorted card.
2. Have we reached the beginning of our array? If so, insert the card.

### Algorithm Analysis

Given our sample data `{7, 2, 5, 8, -3};` on our first pass, we are going to make one comparison: `2` will be compared to `7`, and since `2` is less than `7`, we shift `7` to the right and insert `2` in its place. `5` is not less than `2`, so we will not shift over `2` and will insert `5` before `7` where we created space: we made two comparisons. On our third pass, we will compare `8` with `7`. `8` is not smaller than `7` so we will not shift over any values. We will leave `8` where it is and consider it part of the sorted sub-list. We only made one comparison but could have made up to three if our current element was smaller than any elements in the sorted sub-list. On our final pass, we will compare `-3` to `8`. `-3` is less than `8` so we will shift `8` over. We will next compare `-3` to `7` and shift `7` over. Next, we will compare `-3` to `5`, and shift `5` over. Finally, we will compare `-3` to `2`. `-3` is less than `2` so we will shift `2` over. This was four comparisons.

We made one comparison on our first pass, two comparisons on our second pass, one comparison on our third pass, and then finally four comparisons on our last pass for a total of 8 comparisons. For some of those iterations (like the third one) we got lucky: we didn’t have to do too much work to find the correct place to insert the value. However, in the worst-case scenario, we would need to make `10` total comparisons to completely sort all `5` items in the list.

Imagine the number of comparisons we would need to make with ten pieces of data `{7, 2, 5, 8, -3, 12, 6, 80, 7, -70}`. If we were unlucky and in the worst-case scenario, our last pass would make `9` total comparisons. Now, imagine a thousand pieces of data: as the size of the dataset $N$ gets very big, it turns out that in the worst-case scenario, we need to make $N^2$ comparisons. In general, if you see an algorithm with a nested for-loop, like this one, the algorithm is probably has a runtime of at least $O(N^2)$, if not worse.

Insertion sort does have an interesting best-case scenario where an array is already sorted: insertion sort has a best-case complexity of $O(N)$. Consider the case when the array is already sorted, we still need to insert every card in our hand into its proper place, but every time we check to see where that card should go, we immediately find the correct place. We need to do `1` comparison for each card, giving us a total of $N$ work.

A Java implementation of an integer insertion sort algorithm is shown below:

```java
import java.util.Arrays;

public class InsertionSort {

  public static void sort(int[] array) {
   for (int i = 1; i < array.length; i++) {
     int current = array[i];
     int j = i -1;
     while (j >= 0 && array[j] > current) {
       array[j + 1] = array[j];
       j--;
     }
     array[j + 1] = current;
   }
  }

  public static void main(String[] args) {
    int[] numbers = {7, 2, 14, -7, 72};
    System.out.println("Array in ascending order");
    sort(numbers);
    System.out.println(Arrays.toString(numbers));
  }
}
```

By changing the comparison operator in the `while-loop` from greater-than to less-than, you get a descending order sorted list:

```java
import java.util.Arrays;

public class InsertionSort {
  public static void sort(int[] array) {
   for (int i = 1; i < array.length; i++) {
     int current = array[i];
     int j = i -1;
     while (j >= 0 && array[j] < current) { // operator changed to reflect descending order
       array[j + 1] = array[j];
       j--;
     }
     array[j+1] = current;

   }
  }

  public static void main(String[] args) {
    int[] numbers = {7, 2, 14, -7, 72};
    sort(numbers);
    System.out.println(Arrays.toString(numbers));
  }
}
```

A Java implementation of a string insertion sort algorithm is shown below:

```java
import java.util.Arrays;

public class InsertionSort {

    public static void sort(String[] strArray) { // insertion sort starts from second element
        for (int i = 1; i < strArray.length; i++) {
            String stringToSort = strArray[i];
            int j = i;
            while (j > 0 && strArray[j - 1].compareTo(stringToSort) > 1) { 
                strArray[j] = strArray[j - 1];
                j--;
            } 
                strArray[j] = stringToSort; 
        } 
    }

    public static void main(String[] args) {
        String[] strings = {"Hello", "World", "Code", "Algorithms"};
        sort(strings);
        System.out.println(Arrays.toString(strings));
    }
}

// OUTPUT TERMINAL: [Algorithms, Code, Hellow, World]
```