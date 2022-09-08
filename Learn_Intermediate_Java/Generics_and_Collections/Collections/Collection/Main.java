package Learn_Intermediate_Java.Generics_and_Collections.Collections.Collection;

import java.util.List;
import java.util.ArrayList;
import java.util.Set;
import java.util.HashSet;
import java.util.Queue;
import java.util.LinkedList;
import java.util.Deque;
import java.util.ArrayDeque;
import java.util.Collection;

public class Main {
  public static void main(String[] args) {
    List<Integer> intList = new ArrayList<>(); // Creates a new List implemented as an ArrayList
    Set<String> stringSet = new HashSet<>(); // Creates a new Set implemented as a HashSet
    Queue<Double> doubleQueue = new LinkedList<>(); // Creates a new Queue implemented as a LinkedList
    Deque<Integer> intDeque = new ArrayDeque<>(); // Creates a new Deque implemented as an ArrayDeque

    intList.add(5); // adds 5 to intList
    intList.add(8); // adds 8 to intList
    intList.add(5); // adds 5 to intList
    intList.add(1); // adds 1 to intList

    stringSet.add("Hello"); // adds Hello to stringSet
    stringSet.add("World"); // adds World to stringSet
    stringSet.add("World"); // does nothing as a Set does not contain duplicates

    doubleQueue.add(3.89); // adds 3.89 to doubleQueue
    doubleQueue.add(889.64); // adds 889.64 to doubleQueue

    intDeque.addFirst(7); // adds 7 to the front of intDeque [front] -> 7 <- [back]
    intDeque.addFirst(8); // adds 8 to the front of intDeque [front] -> 8, 7 <- [back]
    intDeque.addLast(40); // adds 7 to the back of intDeque [front] -> 8, 7, 40 <- [back]

    // prints the class of intList to the terminal (ArrayList)
    System.out.println(intList.getClass());
    printCollection(intList);
    System.out.println();

    // prints the class of stringSet to the terminal (HashSet)
    System.out.println(stringSet.getClass());
    printCollection(stringSet);
    System.out.println();

    // prints the class of doubleQueue to the terminal (LinkedList)
    System.out.println(doubleQueue.getClass());
    printCollection(doubleQueue);
    System.out.println();

    // prints the class of intDeque to the terminal (ArrayDeque)
    System.out.println(intDeque.getClass());
    printCollection(intDeque);
  }

  private static <T> void printCollection(Collection<T> collection) {
    
    // enhanced for-loop iterates through each item in the collection given and prints them to the terminal
    for (T item: collection) {
      System.out.println(item);
    }
  }
}