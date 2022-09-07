package Learn_Intermediate_Java.Generics_and_Collections.Generics.Wildcards;

public class Main {
    public static void main(String[] args) {
      Container<String> stringContainer = new Container<>("Hello");
      Container<Integer> intContainer = new Container<>(34);
  
      printContainer(stringContainer);
      printContainer(intContainer);
    }
  
    public static void printContainer(Container<?> container) {
      System.out.println(container.toString());
    }
  }