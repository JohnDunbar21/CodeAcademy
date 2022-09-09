package Java_Algorithms.Recursion.Practical.Introduction;

public class Factorial {
	public static int iterativeFactorial(int n) {
		int result = 1;

        // while the value of n is greater than 0, it will multiply the result variable by the value of n before decrementing the n value
		while (n > 0) {
			result *= n;
			n -= 1;
		}

		return result;
	}
	public static void main(String[] args) {
		int fourFactorial = iterativeFactorial(4);

        // prints the factorial of 4, equaling 24
		System.out.println(fourFactorial);
    
	}
}