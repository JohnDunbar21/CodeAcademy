package Learn_Java.Loops;

import java.util.Random;

public class LuckyFive {
    
    public static void main(String[] args){
        
        // Creating a randum number generator
        Random randomGenerator = new Random();

        // Generate a number between 1 and 6
        int dieRoll = randomGenerator.nextInt(6) + 1;

        while (dieRoll != 5) {
            System.out.println(dieRoll);
            dieRoll = randomGenerator.nextInt(6) + 1;
        }
    }
}
