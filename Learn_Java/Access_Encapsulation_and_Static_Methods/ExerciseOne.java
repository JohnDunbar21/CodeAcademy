package Learn_Java.Access_Encapsulation_and_Static_Methods;

public class ExerciseOne {
    
    public static void main(String[] args){

        int randomNum = (int)(Math.random() * 10) + 1; // the random number algorithm uses (Math.random() * (Max value - Min value + 1)) + Min value
        System.out.println("Your random number between one and ten is " + randomNum);
        
        int negativeNum = -2;
        int absNum = Math.abs(negativeNum);
        System.out.println("The absolute value of "+ negativeNum + " is " + absNum);
    
        String myNewString = Integer.toString(1);
        System.out.println(myNewString);
    
      }
}
