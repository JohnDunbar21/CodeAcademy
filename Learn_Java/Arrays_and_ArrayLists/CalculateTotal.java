package Learn_Java.Arrays_and_ArrayLists;

import java.util.ArrayList;

public class CalculateTotal {
    
    public static void main(String[] args){

        ArrayList<Double> expenses = new ArrayList<Double>();
        expenses.add(74.46);
        expenses.add(63.99);
        expenses.add(10.57);
        expenses.add(81.37);

        double total = 0;

        for (int i = 0; i < expenses.size(); i++){
            total += expenses.get(i);
        }

        System.out.println(total);
    }
}
