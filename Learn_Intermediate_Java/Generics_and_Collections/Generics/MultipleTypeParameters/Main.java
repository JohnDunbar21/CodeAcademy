package Learn_Intermediate_Java.Generics_and_Collections.Generics.MultipleTypeParameters;

public class Main {
    public static void main(String[] args) {
      Container<Integer, Double> myContainer = new Container<>(2, 45.98);
      
      System.out.println("Item1: "+ myContainer.getItem1());
      System.out.println("Item2: "+ myContainer.getItem2());
    }
  }