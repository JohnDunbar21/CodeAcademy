package Learn_Java.Access_Encapsulation_and_Static_Methods;

public class ScopeExample {
    
    public static void main(String[] args){

        int[] myArray = {1, 2, 3, 4};
        // the sum variable was moved from within the for loop as this was outside the scope of the function
        int sum = 0;
        for(int i = 0; i < myArray.length; i++){
          
          sum += myArray[i];
        }
    
        System.out.println(sum);
      }
}
