package Learn_Intermediate_Java.Generics_and_Collections.Collections.Set;

//import java.util.Set;
import java.util.TreeSet;

public class Main {
  public static void main(String[] args) {

    TreeSet<String> stringSet = new TreeSet<>(); // stores elements based on their values

    stringSet.add("Hello");
    stringSet.add("World");
    stringSet.add("Hello");

    for (String element: stringSet) {
      System.out.println(element); // prints each element in the TreeSet to the terminal
    }
  }
}