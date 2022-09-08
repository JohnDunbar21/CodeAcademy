package Learn_Intermediate_Java.Generics_and_Collections.Collections.Algorithms;

import java.util.List;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Collection;
import java.util.Set;
import java.util.HashSet;
import java.util.Iterator;

public class Main {
  public static void main(String[] args) {
    List<Integer> myList = new ArrayList<>(); // Creates a new List implemented as an ArrayList
    
    myList.add(3); // adds 3 to myList
    myList.add(-1); // adds -1 to myList
    myList.add(57); // adds 57 to myList
    myList.add(29); // adds 29 to myList

    Set<String> mySet = new HashSet<>(); // Creates a new Set implemented as a HashSet

    mySet.add("Hello"); // adds Hello to mySet
    mySet.add("World"); // adds World to mySet

    System.out.println("mySet max: \""+ Collections.max(mySet)+"\""); // uses string formatting to print the max() value in mySet to the terminal
    System.out.println();

    System.out.println("myList min: "+ Collections.min(myList)); // uses string formatting to print the min() value in myList to the terminal
    System.out.println();

    System.out.println("Index of 57 in myList is: "+Collections.binarySearch(myList, 57)); // uses binarySearch() and string formatting to print the index value of 57 in myList to the terminal
    System.out.println();


    System.out.println("myList prior to reverse: ");
    printCollection(myList);

    System.out.println();

    Collections.reverse(myList);
    System.out.println("myList reversed: ");
    printCollection(myList);

    System.out.println();

    System.out.println("myList prior to sort: ");
    printCollection(myList);

    System.out.println();

    Collections.sort(myList);
    System.out.println("myList after sort: ");
    printCollection(myList);


  }

  public static void printCollection(Collection<?> collection){
    Iterator<?> myItr = collection.iterator(); // Creates an Iterator with a wildcard type (meaning it can take any type of input such as String, Integer, Boolean, etc), implemented using the iterator() method from Collections

    // while the Collection myItr is not empty, it will print the next value in myItr
    while(myItr.hasNext()){
      System.out.println(myItr.next());
    }
  }
}