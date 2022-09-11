# Selection Sort

### Introduction

Selection sort is an algorithm that selects the smallest item that has not been sorted yet and then implements the sort by finding the correct place to put it. This works by dividing a given input array into two virtual sub-lists: the first sub-list contains every element we have sorted, and the second contains every unsorted element. We select items from the second sub-list and insert them into the first sub-list.

The logic that forms the basis of the selection sort algorithm is:

```
selectionSort(array)
    repeat (size - 1) times
        start at the beginning index of the unsorted sub-list as the current minimum
            walk through all elements of the unsorted sub-list to find the index of the smallest element and set as current minimum
        swap that element with the first element in the unsorted sub-list. That element is now part of the sorted sublist
    end selectionSort
```

Initially, the sorted sub-list is empty and the unsorted sub-list contains all the items.

The algorithm will be implemented with two loops. The first loop will run `size - 1` times because we have to do the process of selecting the smallest item and moving it into the sorted sub-list once for every item in the list. We have a `-1` here because we don't have to do this for the very last item: if every other item in the list has been sorted, the last item is guaranteed to be sorted.

We will store the first position in the unsorted sub-list as our **current minimum**:

Input array: `{2, 7, -7, 20, -5};`

Sorted sub-list: `{};`
Unsorted sub-list: `{2, 7, -7, 20, -5};`
Current minimum: `2`

The inner `for-loop` will iterate through the unsorted sub-list `N` times making comparisons to find the smallest value in the unsorted sub-list. For each comparison of `current minimum` to the remaining items in the unsorted sub-list, the algorithm will check:

* If the unsorted number in comparison is less than our `current minimum`. If it is not, we continue.

Unsorted sub-list: `{2, 7, -7, 20, -5};`
Current minimum: `2`
Next unsorted element: `7` [the current minimum does not change]

If a smaller number is found, set the index as the new `current minimum` and continue to the end of the array.

Unsorted sub-list: `{2, 7, -7, 20, -5};`
Current minimum: `2`
Next unsorted element: `-7` [the current minimum is `-7`]

Unsorted sub-list: `{2, 7, -7, 20, -5};`
Current minimum: `-7`
Next unsorted element: `20` [the current minimum does not change]
Unsorted sub-list: `{2, 7, -7, 20, -5};`
Current minimum: `-7`
Next unsorted element: `-5` [the current minimum does not change]

When we reach the end of the comparisons in the unsorted sub-list, the smallest element is selected and swapped with the first unsorted position, and that element is now considered a part of the sorted sub-list.

Unsorted sub-list: `{2, 7, -7, 20, -5};`
`2` swaps places with`-7`
After swap: `{-7, 7, 2, 20, -5}`

We can consider `-7` to be a part of the sorted sub-list and `2` to be a part of the unsorted sub-list.

We will have to keep track of where the boundary between our unsorted sub-list and sorted sub-list is. Now that we’ve sorted one element, that boundary has moved to the right by one giving us a new current minimum.

Unsorted sub-list: 7, 2, 20, -5
Current minimum: 7

We would then find the next minimum element -5 and swap it to the new start of the unordered list.

Original input array: `{2, 7, -7, 20, -5}`
`-5` swaps places with `7`
After two swaps: `{-7, -5, 2 20, 7}`

We will repeat the process until we have reached the last element in our input array which we will consider to be sorted by the time we have reached it.

### Algorithm Analysis

Let’s consider how much work this algorithm does in order to sort the array. This algorithm makes a lot of comparisons using our two for loops: given our sample data `{2, 7, -7, 20, 5}` on our first pass, we are going to make four comparisons. `2` will first be compared to `7`. `2` is smaller. Then `2` will be compared to `-7`. `-7` becomes our smallest number. We’ll then compare `-7` to `20` and then again to `5`. We’ll make four total comparisons on this pass through the data.

On our next pass, the `-7` has already been sorted, so we only have four items in our unsorted sublist. We’ll have to make three comparisons to find the smallest. On our third pass there will be two comparisons and so on. When we add all of these up, for a list of size 5, that is a total of 10 comparisons. While that doesn’t seem like a ton of comparisons, imagine the amount of comparisons we would need to make with ten pieces of data: `{2, 7, -7, 20, 5, -3, 5, 18, 4, -50}`. Our first pass alone would make nine comparisons. Now, imagine a hundred pieces of data.

In fact, when thinking about the runtime of algorithms, we only care about how they do on absurdly large lists. It turns out that as we get larger and larger lists, the number of comparisons starts to approach $N^2$ (where $N$ is the length of the list).

We can see this happen in our example lists. With a list of size `5`, we needed `10` comparisons. That’s pretty far away from `25` (5^2). When we have a list of size `10`, we need to do `55` total comparisons. That’s getting closer to 10^2. We won’t go through the math here, but as $N$ approaches infinity, the number of comparisons needed approaches $N^2$.

$N^2$ comparisons is pretty bad. Some sorting algorithms can cut out some of their comparisons depending on the array they’re trying to sort, but that isn’t the case for selection sort.

Consider the best case for this sorting algorithm: we give selection sort an already sorted array. Can selection sort cut out any comparisons? Unfortunately, the answer is no. We still need to look through all of our values to find the smallest value. It just so happens that we don’t need to swap it because it’s already in the right place.

Whether we’re given the best case, worst case, or any random list, selection sort will always make $N^2$ comparisons.

Nested loops are generally an indicator of quadratic complexity. This means that as the number of elements $N$ increases, the running time increases quadratically. This means that if $N$ doubles, we know that sorting time will quadruple.

Below is the Java implementationn of a selection sort algorithm for an ascending order integer array:

```java
import java.util.Arrays;

public class SelectionSort {
  public static void selectionSort (int[] arr) {

  int size = arr.length;  
  for (int i = 0; i < size - 1; i++) {
    int currentMinimumIndex = i;
    for (int j = i + 1; j < size; j++) {
      if (arr[j] < arr[currentMinimumIndex]) {
        currentMinimumIndex = j;
      }
    }
    swap(arr, i, currentMinimumIndex);
  }
}

  public static void swap(int[] arr, int indexOne, int indexTwo) {
    int temp = arr[indexTwo];
    arr[indexTwo] = arr[indexOne];
    arr[indexOne] = temp;
 }

  public static void main(String args[]) {
    int[] data = { 2, 7, -7, 20, -5 };
    SelectionSort.selectionSort(data);
    System.out.println("Sorted Array in Ascending Order: ");
    System.out.println(Arrays.toString(data));
  }
}
```

To make this a descending order selection sort algorithm, just change the less-than case in the inner `for-loop` to a greater-than case:

```java
import java.util.Arrays;

public class SelectionSort {
  public static void selectionSort (int arr[]) {
    int size = arr.length;
    for (int i = 0; i < size - 1; i++) {
      int currentMinimumIndex = i;
      for (int j = i + 1; j < arr.length; j++) {
        if (arr[j] > arr[currentMinimumIndex]) {
          currentMinimumIndex = j;
        }
      }
      swap(arr, i, currentMinimumIndex);
  }
}
  public static void swap(int[] arr, int indexOne, int indexTwo) {
    int temp = arr[indexTwo];
    arr[indexTwo] = arr[indexOne];
    arr[indexOne] = temp;
 }
  public static void main(String args[]) {
     int[] data = { 2, 7, 1, 16, 4, 0 };
     SelectionSort.selectionSort(data);
     System.out.println(Arrays.toString(data));
  }
}
```