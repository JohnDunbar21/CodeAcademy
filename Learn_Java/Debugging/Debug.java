package Learn_Java.Debugging;

public class Debug {
    
  public static void main(String[] args) {
    
    try{
      int width = 0; // zero division error will be the issue.
      int length = 40;
      
      int ratio = length / width;
      System.out.println(ratio);
    } catch (ArithmeticException e){
      // 'err' means it looks for the error info instead ouf the 'out' output.
      System.err.println("The arithmetic operation you are trying to perform is invalid.");
    }
  }
  
}
