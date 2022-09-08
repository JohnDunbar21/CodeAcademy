package Learn_Intermediate_Java.Generics_and_Collections.Collections.Map;

import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.util.TreeMap;
import java.util.Random;

public class Main {
  public static void main(String[] args) {
    List<Integer> myInts = new ArrayList<>(); // Creates a new List implemented as an ArrayList
    Random random = new Random(); // Creates a new Random object called random

    // a for loop that starts at 0 and increments by 1 until it reaches 20 that adds a number between 0 and 5 (the bound parameter in the nextInt() method determines this upper bound)
    for(int i =0; i < 20; i++) {
      myInts.add(random.nextInt(5));
    }

    Map<Integer, Integer> intCount = countNumbers(myInts); // Creates a new Map implemented using the countNumbers() custom method

    // enhanced for-loop that iterates through each key-value pair and uses string formatting to print each key-value pair to the terminal
    for(Map.Entry<Integer, Integer> entry: intCount.entrySet()) {
      System.out.println("Integer: "+ entry.getKey()+" appears: "+ entry.getValue());
    }
  }

  // static method that takes a List and returns a Map of Integer key-value pairs
  public static Map<Integer, Integer> countNumbers(List<Integer> list) {
    Map<Integer, Integer> intCount = new TreeMap<>();

    for (Integer i: list) {
      Integer currentCount = intCount.get(i);
      if (currentCount != null) {
        int newCount = currentCount + 1;
        intCount.put(i, newCount);
      } else {
        intCount.put(i, 1);
      }
    }

    return intCount;
  }
}