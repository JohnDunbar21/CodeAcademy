public class Operations {
    public static void main(String[] args) {
        int expression1 = 5 % 2 - (4 * 2 - 1);
        int expression2 = (3 + (2 * 2 - 5)) + 6 - 5;
        int expression3 = 5 * 4 % 3 - 2 + 1;

        /*
        Order of Operation:
        1. Parenthesis
        2. Exponents
        3. Modulo/Multiplication/Division
        4. Addition/Subtraction
        */

        System.out.println(expression1);
        System.out.println(expression2);
        System.out.println(expression3);
    }
}
