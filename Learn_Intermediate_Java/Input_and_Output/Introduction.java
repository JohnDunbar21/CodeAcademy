package Learn_Intermediate_Java.Input_and_Output;

//import java.io.*;

/*
For the printf format:

%s represents a string

%c represents a character

%d represents an integer
*/


public class Introduction {
    public static void main(String[] args){
        String name = "John";
        String hobbies = "coding, reading, problem solving";
        int age = 22;
    
        System.out.println("My name is "+name);
        System.out.printf("I am %d years old. ", age);
        System.out.print("My hobbies are "+hobbies);
    }
}