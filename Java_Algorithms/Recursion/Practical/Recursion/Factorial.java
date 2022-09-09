package Java_Algorithms.Recursion.Practical.Recursion;

public class Factorial {
	public static int recursiveFactorial(int n) {
		if (n > 0) {
			System.out.println("Execution context: " + n);

			recursiveFactorial(n - 1);
		}

		return 0;
	}

	public static void main(String[] args) {
		int recursiveSolution = recursiveFactorial(4);
		System.out.println(recursiveSolution);
	}
}