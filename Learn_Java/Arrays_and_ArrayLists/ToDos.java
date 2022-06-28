package Learn_Java.Arrays_and_ArrayLists;

import java.util.ArrayList;

public class ToDos {
    
    public static void main(String[] args){

        // creating a new ArrayList
        ArrayList<String> toDoList = new ArrayList<String>();

        String toDo1 = "Water plants";
        String toDo2 = "Clean house";
        String toDo3 = "Do shopping";

        toDoList.add(toDo1);
        toDoList.add(toDo2);
        toDoList.add(toDo3);

        System.out.println(toDoList);

        // Sherlock
        ArrayList<String> sherlocksToDos = new ArrayList<String>();
        
        sherlocksToDos.add("visit the crime scene");
        sherlocksToDos.add("play violin");
        sherlocksToDos.add("interview suspects");
        sherlocksToDos.add("solve the case");
        sherlocksToDos.add("apprehend the criminal");
        
        // Poirot
        ArrayList<String> poirotsToDos = new ArrayList<String>();
        
        poirotsToDos.add("visit the crime scene");
        poirotsToDos.add("interview suspects");
        poirotsToDos.add("let the little grey cells do their work");
        poirotsToDos.add("trim mustache");
        poirotsToDos.add("call all suspects together");
        poirotsToDos.add("reveal the truth of the crime");
        
        // Print the size of each ArrayList below:
        System.out.println(sherlocksToDos.size());
        System.out.println(poirotsToDos.size());

        System.out.println("Sherlock's third to-do:");
        // Print Sherlock's third to-do:
        System.out.println(sherlocksToDos.get(2));
        
        System.out.println("\nPoirot's second to-do:");
        // Print Poirot's second to-do:
        System.out.println(poirotsToDos.get(1));

        // Set each to-do below:
        sherlocksToDos.set(1, "listen to Dr. Watson for amusement");
        poirotsToDos.set(3, "listen to Captain Hastings for amusement");
        
        System.out.println("Sherlock's to-do list:");
        System.out.println(sherlocksToDos.toString() + "\n");
        System.out.println("Poirot's to-do list:");
        System.out.println(poirotsToDos.toString());

        // Remove each to-do below:
        sherlocksToDos.remove(0);
        poirotsToDos.remove(0);
        sherlocksToDos.remove(0); // this is 0 now as the original 0 value was removed prior to this item
        
        
        System.out.println(sherlocksToDos.toString() + "\n");
        System.out.println(poirotsToDos.toString());

        System.out.println(sherlocksToDos.indexOf("solve the case")); // retrieves the index of the value being queried.
    }
}
