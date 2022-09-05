package Learn_Intermediate_Java.Input_and_Output;

import java.util.Scanner;

/* 
The 'Scanner' class can read different types of values than can be saved into different variable types.
Below are some examples (not all) of the different variable types and the code required to read the
variables into the program:

- Integer:
    int num = input.nextInt();

- Double:
    double numDouble = input.nextDouble();

- Byte:
    byte numByte = input.nextByte();

- Boolean:
    boolean isTrue = input.nextBoolean();

- Long:
    long numLong = input.nextLong();

- Short:
    short numShort = input.nextShort();


The 'Scanner' class also has many functions, including the ability to validate and convert variables.
Some examples include:

input.hasNextLine();

The above command is a function that returns a boolean that validates if there is another line in the 
input of the defined scanner.

input.hasNextInt();

The above command is a function that returns a boolean that validates if there is another integer in
the input of the defined scanner.

input.useDelimiter(",");

The above command helps us spefify what delimiters we want to use (a unit used to separate data units).
This is especially helpful when programs are required to parse through csv files.

num.toString();

The above command assumes that the variable num is an integer, and the attached method converts it to a
string value. The command can be used on any type of variable.
*/

public class InputOutput {
    public static void main(String[] args){
        try (Scanner input = new Scanner(System.in)) {
            System.out.println("Please enter your username:");
            String userName = input.next();
            System.out.printf("Hello %s! It's nice to meet you.", userName);
        }
    }
}