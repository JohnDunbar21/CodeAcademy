public class Main {
    public static void main(String[] args) {
      String myWord = "Hello";
      Book myBook = new Book("My Book");
      // Create `Container` references and print statement below...
      Container<String> wordContainer = new Container<>(myWord);
      Container<Book> bookContainer = new Container<>(myBook);
  
      System.out.println("Word Container Data: "+ wordContainer.getData());
      System.out.println("Book Container Data: "+ bookContainer.getData());  
    }
  }