package Learn_Intermediate_Java.Input_and_Output.FileOutputStream;

import java.io.*;

/*
1. Declare your output stream using FileOutputStream.

2. Write to your file, this can be done as shown below.

3. Close the file using java.io's close() method.
*/

public class WritingFiles {
    public static void main(String[] args) throws IOException {
        FileOutputStream outputFile = new FileOutputStream("output.txt");
        String outputText = "This is my first file written using the Java language!";

        outputFile.write(outputText.getBytes());
        outputFile.close();
    }
}
