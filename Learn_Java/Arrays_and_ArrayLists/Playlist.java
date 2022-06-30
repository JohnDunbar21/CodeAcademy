package Learn_Java.Arrays_and_ArrayLists;

import java.util.ArrayList;

public class Playlist {
    
    public static void main(String[] args){

        ArrayList<String> desertIslandPlaylist = new ArrayList<String>(); // creates and initialises an ArrayList of String type

        // a list of song items to add to the ArrayList: these will appear in the order they are added
        desertIslandPlaylist.add("What Could Have Been");
        desertIslandPlaylist.add("Vordt of the Boreal Valley");
        desertIslandPlaylist.add("Sea of Lanterns");
        desertIslandPlaylist.add("Relaxation in Liyue");
        desertIslandPlaylist.add("Dynasties and Dystopias");
        desertIslandPlaylist.add("Flight of the Silverbird");

        //System.out.println(desertIslandPlaylist.size()); // checks the number of items in the ArrayList
        System.out.println("You currently have "+desertIslandPlaylist.size()+" songs in your playlist.");

        // the playlist can now only be five songs, so some must be removed until five remain
        desertIslandPlaylist.remove(4); // removes the 5th item in the ArrayList

        //System.out.println(desertIslandPlaylist.size());
        System.out.println("You currently have "+desertIslandPlaylist.size()+" songs in your playlist.");
        System.out.println("Your playlist is currently:");
        System.out.println(desertIslandPlaylist);

        // changing the order of two songs
        int songA = desertIslandPlaylist.indexOf("Vordt of the Boreal Valley");
        int songB = desertIslandPlaylist.indexOf("Flight of the Silverbird");

        String tempA = "Vordt of the boreal Valley";

        desertIslandPlaylist.set(songA, "Flight of the Silverbird");
        desertIslandPlaylist.set(songB, tempA);
        
        System.out.println("Your playlist after reorganising two of the songs is:");
        System.out.println(desertIslandPlaylist);
    }
}
