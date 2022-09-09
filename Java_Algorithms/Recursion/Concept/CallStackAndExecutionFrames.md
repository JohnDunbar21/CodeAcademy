# Call Stacks and Execution Frames

A recursive approach requires the function invoking itself **with different arguments**.

Languages make this possible with **call stacks** and **execution contexts**.

Stacks, a data structure, follow a strict protocol for the order data enters and exits the structure: **the last thing to enter is the first thing to leave** (LIFO). The call stack exists outside of any specific function, and can track the ordering of the different function invocations, so that the **last function to enter the call stack is the first function to exit the call stack**.

Think of execution contexts as the specific values we plug into a function call.

```
A function which adds two numbers:
 
Invoking the function with 3 and 4 as arguments...
execution context:
X = 3
Y = 4
 
Invoking the function with 6 and 2 as arguments...
execution context:
X = 6
Y = 2
```

Consider the pseudocode below which sums the integers in an array:

```
function, sum_list 
    if list has a single element
        return that single element
    otherwise...
        add first element to value of sum_list called with every element minus the first
```

In a nutshell, this function will be invoked as many times as there are elements within the array!

```
CALL STACK EMPTY
___________________
 
Our first function call...
sum_list([5, 6, 7])
 
CALL STACK CONTAINS
___________________
sum_list([5, 6, 7])
with the execution context of a list being [5, 6, 7]
___________________
 
Base case, a list of one element not met.
We invoke sum_list with the list of [6, 7]...
 
CALL STACK CONTAINS
___________________
sum_list([6, 7])
with the execution context of a list being [6, 7]
___________________
sum_list([5, 6, 7])
with the execution context of a list being [5, 6, 7]
___________________
 
Base case, a list of one element not met.
We invoke sum_list with the list of [7]...
 
CALL STACK CONTAINS
___________________
sum_list([7])
with the execution context of a list being [7]
___________________
sum_list([6, 7])
with the execution context of a list being [6, 7]
___________________
sum_list([5, 6, 7])
with the execution context of a list being [5, 6, 7]
___________________
 
We've reached our base case! List is one element. 
We return that one element.
This return value does two things:
 
1) "pops" sum_list([7]) from CALL STACK.
2) provides a return value for sum_list([6, 7])
 
----------------
CALL STACK CONTAINS
___________________
sum_list([6, 7])
with the execution context of a list being [6, 7]
RETURN VALUE = 7
___________________
sum_list([5, 6, 7])
with the execution context of a list being [5, 6, 7]
___________________
 
sum_list([6, 7]) waits for the return value of sum_list([7]), which it just received. 
 
sum_list([6, 7]) has resolved and "popped" from the call stack...
 
 
----------------
CALL STACK contains
___________________
sum_list([5, 6, 7])
with the execution context of a list being [5, 6, 7]
RETURN VALUE = 6 + 7
___________________
 
sum_list([5, 6, 7]) waits for the return value of sum_list([6, 7]), which it just received. 
sum_list([5, 6, 7]) has resolved and "popped" from the call stack.
 
 
----------------
CALL STACK is empty
___________________
RETURN VALUE = (5 + 6 + 7) = 18
```