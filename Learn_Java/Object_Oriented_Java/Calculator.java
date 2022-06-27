package Learn_Java.Object_Oriented_Java;

public class Calculator {
    /*
    In this assessment, you will use classes, methods, and objects to create a simple arithmetic calculator.
    This must be able to perform:
    - Addition
    - Subtraction
    - Multiplication
    - Division
    - Modulus
     */

     //Class constructor
     public Calculator(){

     }

     public int add(int a, int b){
        return a + b;
     }

     public int subtract(int a, int b){
        return a - b;
     }

     public int multiply(int a, int b){
        return a * b;
     }

     public double divide(int a, int b){
        return a / b;
     }

     public int modulo(int a, int b){
        return a % b;
     }

     public static void main(String[] args){
        Calculator myCalculator = new Calculator();
        System.out.println(myCalculator.add(5, 7));
        System.out.println(myCalculator.subtract(45, 11));
     }
}
