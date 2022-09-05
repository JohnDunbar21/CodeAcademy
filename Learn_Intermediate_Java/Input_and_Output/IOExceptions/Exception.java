package Learn_Intermediate_Java.Input_and_Output.IOExceptions;

import java.io.*;

/*
IOExceptions are exceptions that are related to input and/or output in a program and can be classified as checked exceptions.

Some examples of when IOExceptions occur include:

- Failed attempts at trying to access a file.

- The end of a file has been reached.

- The file a program is attempting to access cannot be found.

- An input/output operation has been interrupted.

Instead of a try-catch block, we can also use the keyword throws so that the exception is handled by the program itself.
*/

public class Exception {
    public static void main(String[] args){
        String path = "/home/ccuser/workspace/java-input-and-output-file-input-stream/input.txt";
        try {
          FileInputStream inputFile = new FileInputStream(path);
          int i = 0;    
          while((i = inputFile.read()) != -1) {    
            System.out.print((char)i);    
          }    
          inputFile.close();
        } catch (IOException e) {
          System.out.println("There has been an IO exception!");
          System.out.println(e);
        }
      }
}
