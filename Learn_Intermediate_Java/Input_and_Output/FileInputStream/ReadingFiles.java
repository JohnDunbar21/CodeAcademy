package Learn_Intermediate_Java.Input_and_Output.FileInputStream;

import java.io.*;

/*
1. Declare your input stream using FileInputStream.

2. Read the file, this can be done using a while loop as shown below.

3. Close the file using java.io's close() method.
*/

public class ReadingFiles {
    public static void main(String[] args) throws IOException{
        String path = "Learn_Intermediate_Java/Input_and_Output/FileInputStream/input.txt";
        FileInputStream inputFile = new FileInputStream(path);
        int counter = 0;
        while((counter = inputFile.read()) != -1) {
          System.out.print((char)counter);
        }
        inputFile.close();
    }
}
