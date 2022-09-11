# Merge Sort

### What is Merge Sort?

The merge sorting algorithm was created by John von Neumann in 1945, and is designed to break a list into smaller parts, and is sometimes referred to as a **divide-and-conquer algorithm**. Merge sort was the first to implement this strategy, and is used regularly in various modern applications.

<img title="" alt="" src="https://content.codecademy.com/courses/merge-sort/merge_ex_3.svg">

### How to Merge Sort

The merge sorting algorithm takes two steps:

1. Split the data into "runs", or smaller components,
2. Re-combine the runs into sorted lists (the "merge").

When splitting data, we divide our input in half, then recursively call the sort on each of those halves, which then cuts the halves into quarters. This process continues until all of the lists only contain a single element, and then the merging begins. 

When merging two single-element lists, we check if the first element is smaller or larger than the other, then return the two-element list with the smaller element followed by the larger element.

<img title="" alt="" src="https://content.codecademy.com/courses/merge-sort/merge_ex_1.svg">

### Merging

When merging pre-sorted lists, we build similarly to how we did with the single-element lists. Let's call the two lists `left` and `right`. Both `left` and `right` are already sorted, so we want to combine them (to **merge** them) into a larger sorted list, let's call it `both`. In order to accomplish this, we need to iterate through both with two indices, `left_index` and `right_index`. At the start, `left_index` and `right_index` both point to the start of their respective lists: `left_index` points to the smallest element of `left`, and `right_index` points to the smallest element of `right`. We compare the elements at `left_index` and `right_index`, where the smaller of these two elements should be the first element of `both` because it is the smallest of both.

Let's say the smallest value was in `left`: we continue by incrementing `left_index` to point to the next smallest value in `left`, then we compare the second smallest value in `left` to the smallest value in `right`. Whichever of the two is smaller becomes the second value of `both`.

This process continues on for as long as both lists have elements to compare, and once one list has been exhausted, say every element from `left` had been added to the result, then we know that the elements of the other list, `right`, should go at the end of the resulting list as they are larger than every element we have seen so far.

<img title="" alt="" src="https://content.codecademy.com/courses/merge-sort/merge_ex_2.svg">

### Merge Sort Performance

Merge sort has all of its time complecities the same: $\Theta(N*\log(N))$. This means that an almost-sorted list will take the same amount of time as a completely out-of-order list.

Merge sort requires a great deal of space as each separation requires a temporary array, and so a merge sort would require enough space to svae the whole of the input a second time. This means the worst-case space complexity of this algorithm is $O(N)$.

Below is a Java implementation of a merge sort algorithm on an integer array:

```java
import java.util.Arrays;

public class MergeSort {

    public static void mergeSort(int[] array) {
        mergeSort(array, 0, array.length - 1);
    }

    private static void mergeSort(int[] array, int start, int end) {

        // Break problem into smaller arrays by calling the function recursively
        int mid = (start + end) / 2;
        if (start < end) {
            mergeSort(array, start, mid);
            mergeSort(array, mid + 1, end);
        }

        // Merge the sorted pieces to get the final solution
        int i = 0;
        int first = start;
        int last = mid + 1;

        int[] temp = new int[end - start + 1];

        while (first <= mid && last <= end) {
            temp[i++] = array[first] < array[last] ? array[first++] : array[last++];
        }
        while (first <= mid) {
            temp[i++] = array[first++];
        }
        while (last <= end) {
            temp[i++] = array[last++];
        }
        i = 0;
        while (start <= end) {
            array[start++] = temp[i++];
        }
    }

    public static void main(String[] args) {
        int[] inputArray = {87, 57, 370, 110, 90, 610, 2, 710, 140, 203, 150};

        System.out.println("Array before Merge Sort:");
        System.out.println(Arrays.toString(inputArray));

        mergeSort(inputArray);

        System.out.println("Array after Merge Sort:");
        System.out.println(Arrays.toString(inputArray));
    }
}
```