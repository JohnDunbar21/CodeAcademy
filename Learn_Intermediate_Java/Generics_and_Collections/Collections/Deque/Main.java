package Learn_Intermediate_Java.Generics_and_Collections.Collections.Deque;

import java.util.Deque;
import java.util.ArrayDeque;
import java.util.List;
import java.util.ArrayList;

public class Main {
  public static void main(String[] args) {
    List<Integer> myInts = new ArrayList<>();
    myInts.add(9);
    myInts.add(13);
    myInts.add(2);
    myInts.add(1);
    myInts.add(11);
    myInts.add(39);
    myInts.add(78);
    myInts.add(4);

    Deque<Integer> result = separateInts(myInts);

    // enhanced for-loop iterating through the variable 'result' and printing each value to the terminal
    for(Integer i: result) {
      System.out.println(i);
    }
  }

  public static Deque<Integer> separateInts(List<Integer> integers){
    Deque<Integer> separatedDeque = new ArrayDeque<>(); // Creates a new Deque implemented by an ArrayDeque

    // enhanced for-loop iterating through the integers and checking if they are even: if they are, they are added to the front of the Deque, otherwise they are added to the back
    for (Integer myInt: integers) {
      if (myInt % 2 == 0) {
        separatedDeque.addFirst(myInt);
      } else {
        separatedDeque.addLast(myInt);
      }
    }

    return separatedDeque;
  }
}