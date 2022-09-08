package Learn_Intermediate_Java.Generics_and_Collections.Collections.AggregateOperations;

import java.util.List;
import java.util.ArrayList;
import java.util.stream.Collectors;

public class Main {
  public static void main(String[] args) {
    List<String> words = new ArrayList<>(); // Creates a new List implemented as an ArrayList

    words.add("Tree");
    words.add("Hello");
    words.add("World");
    words.add("Race");
    words.add("Game");
    words.add("Numbers");
    words.add("Ride");

    List<String> specialWordsWithForLoop = getSpecialWordsWithForLoop(words);

    List<String> specialWordsWithPipeline = getSpecialWordsWithPipeline(words);

    System.out.println("Special Words retrieved from for loop: "+ specialWordsWithForLoop);

    System.out.println("Special Words retrieved from pipeline: "+ specialWordsWithPipeline);

  }

  // a static method that takes a List parameter and iterates through each item, and if that item has a length of 4, it is uppercased and inserted into a local list which is then returned
  public static List<String> getSpecialWordsWithForLoop(List<String> words){
    List<String> specialWords = new ArrayList<>();

    for(String word: words) {
      if (word.length() == 4) {
        String upperCaseWord = word.toUpperCase();
        specialWords.add(upperCaseWord);
      }
    }
    return specialWords;
  }

  // aggregate function 'lambda function' of the above code
  public static List<String> getSpecialWordsWithPipeline(List<String> words){
    List<String> specialWords = words.stream().filter(word -> word.length() == 4).map(word -> word.toUpperCase()).collect(Collectors.toList());

    return specialWords;
  }
}