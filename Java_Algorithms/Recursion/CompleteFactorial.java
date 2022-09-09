package Java_Algorithms.Recursion;

public class CompleteFactorial {

    public static int recursiveFactorial(int n) {
		if (n > 0) {
			return n * recursiveFactorial(n - 1); // adds another function to the callStack
		} else {
			return 1;
		}
	}

	public static int iterativeFactorial(int n) {
		int result = 1;

		while (n > 0) {
			result *= n;
			n -= 1;
		}

		return result;
	}

	public static void main(String[] args) {
		int recursiveSolution = recursiveFactorial(4);
		System.out.println("The recursive solution to 4! is: " + recursiveSolution);

		int iterativeSolution = iterativeFactorial(5);
		System.out.println("The iterative solution to 5! is: " + iterativeSolution);
	}
}
