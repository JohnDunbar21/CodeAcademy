package Learn_Java.Loops;

public class Coffee {
    
    public static void main(String[] args){

        int cupsOfCoffee = 1;

        while (cupsOfCoffee <= 100){
            System.out.println("Fry drinks cup of coffee #"+cupsOfCoffee);
            cupsOfCoffee++;
        }

        // i is initialised as 0, and while i is < 3, it will loop and increment by 1 on each loop.
        for (int i = 0; i < 3; i++){
            System.out.println("i is now "+i);
        }
    }
}
