package Learn_Java.Arrays_and_ArrayLists;

import java.util.Arrays;

public class Newsfeed_V2 {
    
    String[] topics;

    public Newsfeed_V2(String[] initialTopics){
        topics = initialTopics;
    }

    public static void main(String[] args){
        Newsfeed_V2 feed;
        if (args[0].equals("Human")){
            String[] humanTopics = {"Politics", "Science", "Sports", "Love"};
            feed = new Newsfeed_V2(humanTopics);
        } else if (args[0].equals("Robot")){
            String[] robotTopics = {"Oil", "Parts", "Algorithms", "Love"};
            feed = new Newsfeed_V2(robotTopics);
        } else{
            String[] genericTopics = {"Opinion", "Tech", "Science", "Health"};
            feed = new Newsfeed_V2(genericTopics);
        }

        System.out.println("The topics in this feed are:");
        System.out.println(Arrays.toString(feed.topics));
    }
}
