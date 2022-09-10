# Linear Search

## Introduction

In computer science, search algorithms are methodic procedures that locate and retrieve information from a set of data. The **linear search**, otherwise known as the **sequential search**, algorithm sequentially checks whether a given value is an element of a specified list by scanning the elements of a list individually. It will check every item in the list in order from the start to the end until it finds the target value. If it finds the target value in the set of data, the linear search stops and returns the position of the target value in the set of data. However, if it does not find the value, the linear search returns a message stating that the target value is not in the set of data.

## Finding Elements in Lists

Linear search can be used to find a desired value in a list, and does so by examining each of the elements and comparing it with the search element, starting with the first and ending with the last, until it finds the target value.

The steps are:

1. Examine the first element of the list.
2. If the first element is equal to the target value, stop.
3. If the first element is not equal to the target value, check the next element in the list.
4. Continue steps 1-3 until the element is found or the end of the list is reached.

For example, we can use a linear search algorithm to find the target value 22 in a list of integers. The algorithm iteratively moves through the list until it finds the target value of 22 in the list.

```java
public class Example {

    public static int linearSearchInts(int[] lst, int target) {
        for (int i = 0; i < lst.length; i++) {
            if (lst[i] == target) {
                return i;
            }
        }
        return -1; // if the target value is not in the dataset, return -1 
    }
        
    

    public static void main(String[] args) {
        int[] listInts = {1, 10, 23, 94, 83, 35, 22, 44, 23, 67};

        int target = 22;
        int positionOfTarget = linearSearchInts(listInts, target);
        
        if (positionOfTarget == -1) {
            System.out.println("Your target value,"+target+", does not exist in the dataset.");
        } else {
            System.out.println("The index of your target is: "+positionOfTarget);
        }
            
    }
}

// TERMINAL OUTPUT: The index of your target is: 6
```

## Best Case Performance

Linear search is not considered the most efficient search algorithm, especially for very large lists. However, linear search is a good choice if you anticipate finding the target value at the beginning of the list, or if the list is small.

The best case performance for linear search occurs when the target value exists and is the first position of the list: in this case, the linear search has a runtim of $O(1)$. This is because it only has to make a direct reference to the first item in the list and does not have to iterate through its body.

## Worst Case Performance

There are two worst cases for linear searches:

* **Case 1**: when the target value is at the end of the dataset.
* **Case 2**: when the target value does not exist in the list.

In both cases, the linear search algorithm is required to scan the entire dataset of `N` elements and therefore makes `N` comparisons. Therefore the runtime (time complexity) of this algorithm is $O(N)$.

## Average Case Performance

If linear search was used 1,000 times on 1,000 different lists, most searches would be neither best nor worst case time complexities, but rather somewhere in between.

On average, the target value would be somewhere in the middle of the list whose search time would take $O(N/2)$ time. We can prove this.

Each element of the list below requires a different number of comparisons in order to be located: the first element with one comparison, the second is located with two, and so on until the last element is located in `N`, the size of the list, comparisons.

<img title="" alt="" src="https://content.codecademy.com/PRO/skill-paths/jsip/linear_search/1DSearch.svg">

The average case performance is the average number of comparisons, and to calculate this you use the formula below:

$\frac{sum of the number of comparisons for each element}{the number of elements in the list}$

The formal proof of this is:

$E[X] = \displaystyle\sum_{x=1}^{N} xp(x) = \displaystyle\sum{x=1}^{N} \frac{x}{N} = \frac{1}{N} + \frac{2}{N} + ... + \frac{N}{N} = \frac{N+1}{2}$

Simplified, this becomes:

$\frac{N}{2}$

We would expect on average that the linear search algorithm finds its target value halfway through the list, and therefore the average case is $O(N/2)$. That being said, based on big O simplification rules, we remove any constants, which leaves us with the runtime of $O(N)$.

