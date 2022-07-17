package Learn_Java.Two_Dimensional_Arrays;

import java.util.Arrays;
public class Review {
	public static void main(String[] args) {  

		//First, declare and initialize a 4x3 2D array of doubles called `scores` which will contain the exam data for four students. The rows will represent the student and the columns will represent the exam number. You already know the first exam scores (80.4, 96.2, 100.0, 78.9). Use initializer lists to store the first exam scores in the first column and -1 for the remaining exams. Use the provided print statement to print the result in the console.
  double[][] scores = {
    {80.4, -1, -1},
    {96.2, -1, -1},
    {100.0, -1, -1},
    {78.9, -1, -1}
  };


  System.out.println(Arrays.deepToString(scores));

	//The next set of exams have occurred. Using 4 lines of code, manually enter the scores (89.7, 90.5, 93.6, 88.1) for the second exam (column 1). Use the provided print statement to print the updated 2D array as well.
  scores[0][1] = 89.7;
  scores[1][1] = 90.5;
  scores[2][1] = 93.6;
  scores[3][1] = 88.1;

  System.out.println(Arrays.deepToString(scores));
		
  //You have realized that you will only be keeping track of 2 exam grades instead of 3. Declare and initialize an empty 4x2 2D array of double values  called newScores
  double[][] newScores = new double[4][2];


  //Using loops, copy all of the scores for exam 1 and 2 into the new 2D array. (do not include the -1 values)
  for (int i = 0; i < newScores.length; i++){
    for (int j = 0; j < newScores[i].length; j++){
      newScores[i][j] = scores[i][j];
    }
  }

  System.out.println(Arrays.deepToString(newScores));

  //You have allowed the students to complete an extra credit activity to contribute towards their scores. For all exam grades less than 90, add 2 additional points to the grade in `newScores`
  for (int i = 0; i < newScores.length; i++){
    for (int j = 0; j < newScores[i].length; j++){
      if (newScores[i][j] < 90){
        newScores[i][j] += 2;
      }
    }
  }

  System.out.println(Arrays.deepToString(newScores));
	}
}
