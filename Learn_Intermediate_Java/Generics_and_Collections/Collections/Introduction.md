# Introduction to Collections in Java

In Java we often need to write programs that work with groups (or collections) of objects. Recall that an array is an object that holds multiple objects of the same type (also known as its **elements**) but is limited by its fixed size and functionality. Java provides a **Collection Framework** to help overcome the limits of an array and provide more complex functionality to meet different collection needs.

The collection framework provides data structures (through interfaces and implementing classes) and algorithms, which perform common tasks on collections. The collection framework allows us to focus on the important parts of our program and not low-level implementation details such as implementing a dynamic sizing collection.

The collection framework provides a heirarchical relationship between its interfaces, making the various implementations compatible with each other and thus making our code scalable and flexible. All the interfaces in the collections framework are generic, which allows us to use optimised and tested 'plumbing' for our specific data types.


```
                                                            HashSet (Class [extends keyword])
                                                               |
                                                      _________|_____ LinkedHashSet (Class [extends keyword])
                                                      |
                Set (Interface [implements keyword]) <|
                         |                            |_____________________ SortedSet (Interface [implements keyword]) <-- TreeSet (Class [extends keyword])
                         |
                         |
                         |          ____ Priority Queue (Class [extends keyword])
                         |         |
Iterable <-- Collection <|- Queue <|
                         |         |______ Deque (Interface [implements keyword]) <-----------------------|
                         |                                                                                |
                         |                                                                                |
                         |                                                                                |
                         |                                                                                |-- ArrayDeque (Class [extends keyword])
                List (Interface [implements keyword]) <----|                                              |
                                                           |____ ArrayList (Class [extends keyword])      |
                                                           |                                              |
                                                           |____ LinkedList (Class [extends keyword]) <---|
                                                           |
                                                           |____ Vector (Class [extends keyword]) <-- Stack (Class [extends keyword])
```