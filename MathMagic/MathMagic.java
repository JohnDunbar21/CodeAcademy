package MathMagic;

public class MathMagic {
    public static void main(String[] args) {
        int myNumber = 4; // This number will be referred to throughout the code.
        int stepOne = myNumber * myNumber;
        int stepTwo = stepOne + myNumber;
        int stepThree = stepTwo / myNumber;
        int stepFour = stepThree + 17;
        int stepFive = stepFour - myNumber;
        int stepSix = stepFive / 6;

        System.out.println(stepSix);

        /*
        No matter what number myNumber is assigned as, it will always yield the number 3 as a result.
        */

    }
}
