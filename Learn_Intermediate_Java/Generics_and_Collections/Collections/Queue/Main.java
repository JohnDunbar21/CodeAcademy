package Learn_Intermediate_Java.Generics_and_Collections.Collections.Queue;

import java.util.Queue;
import java.util.LinkedList;
import java.util.PriorityQueue;
public class Main {
  public static void main(String[] args) {
    Queue<String> line = new LinkedList<>(); // Creates a new Queue implemented as a LinkedList
    line.add("Mike"); // adds Mike. LinkedList contents: Mike
    line.add("Isabel"); // adds Isabel. LinkedList contents: Mike, Isabel
    line.add("Jenny"); // adds Jenny. LinkedList contents: Mike, Isabel, Jenny

    // enhanced for-loop iterates through each item in the Queue
    for(String name: line) {
      System.out.println(name);
    }

    processAlphabetically(line); // calls the below function...

  }

  public static void processAlphabetically(Queue<String> queue) {
    Queue<String> alphabeticalQueue = new PriorityQueue<>(); // Creates a new Queue implemented as a PriorityQueue

    // enhanced for-loop iterates through given queue and adds them to the PriorityQueue which sets them in their natural order (alphabetical in this case)
    for (String name: queue) {
      alphabeticalQueue.offer(name);
    }

    // while the PriorityQueue is not empty, it will assign the current head from the PriorityQueue to headElement and then print it out
    while (alphabeticalQueue.peek() != null) {
      String headElement = alphabeticalQueue.poll();

      System.out.println("Processing: "+headElement);
    }
  }
}