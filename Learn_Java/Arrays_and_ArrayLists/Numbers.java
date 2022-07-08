package Learn_Java.Arrays_and_ArrayLists;

public class Numbers {
    
    public static void main(String[] args){
        for (int i = 0; i < 100; i++){
            if (i % 5 != 0){
                continue;
            }
            System.out.println(i);
        }
    }
}
