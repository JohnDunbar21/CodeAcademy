package Learn_Intermediate_Java.Generics_and_Collections.Generics.InterfacesGenerics;

public class Main {
    public static void main(String[] args) {
      int myNumber = 24;
      String bookName = "Hello Book!";
      // Enter your code below...
  
      Retriever<Integer> containerRetriever = new Container<>(myNumber);
      Retriever<String> bookRetriever = new Book(bookName);
  
      System.out.println("Container retrieved data: "+ containerRetriever.retrieveData());
      System.out.println("Book retrieved data: " + bookRetriever.retrieveData());
    }
  }