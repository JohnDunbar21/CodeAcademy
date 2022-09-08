package Learn_Intermediate_Java.Generics_and_Collections.Collections.List;

//import java.util.List;
import java.util.ArrayList;
public class Main {
  public static void main(String[] args) {

    ArrayList<String> stringList = new ArrayList<>();

    stringList.add("Hello");
    stringList.add("World");
    stringList.add("!");

    for (String element: stringList) {
      System.out.println(element);
    }
  }
}