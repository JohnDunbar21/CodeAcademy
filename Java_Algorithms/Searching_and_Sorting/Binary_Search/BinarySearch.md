# Binary Search

With an ordered dataset we can implement a binary search which performs the following steps:

1. Check the middle value of the dataset.
2. If this value matches our target value, we can return the index.
3. If the middle value is less than our target value, repeat step 1 using the right half of the list.
4. If the middle value is greater than our target value, repeat step 1 using the left half of the list.

Following this procedure, we can achieve a runtime of $O(\log N)$ as we are cutting the list in half on each iteration. For example, a sorted list of `64` elements will take at most $\log_2 (64) = 6$ comparisons. In the worst case:

* Comparison 1: We look at the middle of all `64` elements

* Comparison 2: If the middle is not equal to our search value, we would look at `32` elements.

* Comparison 3: If the new middle is not equal to our search value, we would look at `16` elements.

* Comparison 4: If the new middle is not equal to our search value, we would look at `8` elements.

* Comparison 5: If the new middle is not equal to our search value, we would look at `4` elements.

* Comparison 6: If the new middle is not equal to our search value, we would look at `2` elements.

When there are `2` elements, the target value is either one or the other, and thus there can be at most `6` comparisons in a sorted list of size `64`.

<img title="" alt="" src="https://content.codecademy.com/courses/updated_images/BinaryComplexity_Updated_1-01.svg">

It is important to note that binary searches only work with lists that are already sorted. If we had an unsorted list, our greater-than and less-than operations would be meaningless.

Let's explore an example: find the number `27` in the following list: `int[] lst = {3, 4, 12, 17, 22, 27, 28, 36, 50};`.

* We start by checking the middle of the list and see if it is our target value: `22` != `27`.
* We move to the right hand side of the array as `22` is less than `27`, so our search area becomes {27, 28, 36, 50}.
* We check if the middle of this section is our target value: `28` != `27`.
* We move to the left hand of the side of the remaining array as `28` is greater than `27`, so our search area becomes {27}.
* We check to the middle of this section, and since it is the only value left, we can conclude that the element `27` = `27`.
* We return the index `5` where the number `27` is located.

### Recursive Binary Search

There are many ways to implement a recursive binary search, but the general steps are:

1. Create an integer variable `mid` that will be used to pick the midpoint index of the given array.
2. Create a base case that checks if our `target` value is equal to the value of our array at `mid`, and if it is then return `mid`.
3. Create two recursive conditions:
    * Check if `target` is less than the value of our array at index `mid`. If `true` then return the value of recursively calling `binarySearch()`, passing in values to search the left half of the array.
    * Check if `target` is greater than the value of our array at index `mid`. If `true` then return the value of recursively calling `binarySearch()`, passing in values to search the right half of the array.
4. Create another base case that checks if our search space has been exhausted: if this happens, we will return `-1`, which will trigger a notice message that the element could not be located.

Below is the Java implementation of a recursive binary search across an array of integers:

```java
public class BinarySearchRecursive {
    public static int binarySearch(int[] array, int left, int right, int target) {
        if (left > right) {
            return -1;
        }

        int mid = left + (right - left) / 2;

        // Base condition if the value is found
        if (target == array[mid]) {
            return mid;
        }

        // Discard all elements in the right of the search area including the mid element
        if (target < arr[mid]) {
            return binarySearch(array, left, mid -1, target);
        }

        // Discard all elements in the left of the search area including the mid element
        if (target > arr[mid]) {
            return binarySearch(array, mid + 1, right, target);
        }
    }

    public static void main(String[] args) {
        int[] arr = {2, 5, 6, 8, 9, 10};
        int target = 8;

        int left = 0;
        int right = arr.length - 1;

        int index = binarySearch(arr, left, right, target);
        if (index != -1) {
            System.out.println("Element found at index: "+index);
        } else {
            System.out.println("Element not found in the given array.");
        }
    }
}
```

The iterative binary search follows the same algorithm, but in a slightly different manner:

```java
public class BinarySearchIterative {
    public static int binarySearch(int[] array, int target) {
        int left = 0;
        int right = array.length - 1;

        while (left <= right) {
            int mid = (left + right) / 2;

            if (target == array[mid]) {
                return mid;
            }

            if (target < array[mid]) {
                return mid -1;
            }

            if (target > array[mid]) {
                return mid + 1;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        int[] arr = {2, 5, 6, 8, 9, 10};
        int target = 6;

        int index = binarySearch(arr, target);
        if (index != -1) {
            System.out.println("Element found at index: "+index);
        } else {
            System.out.println("Element not found in the array.");
        }
    }
}
```