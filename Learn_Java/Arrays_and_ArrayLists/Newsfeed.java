package Learn_Java.Arrays_and_ArrayLists;

import java.util.Arrays;

public class Newsfeed {

    String[] topics = {"Opinion", "Tech", "Science", "Health"};
    int[] views = {0, 0, 0, 0};
    String[] favouriteArticles;
    
    // class constructor
    public Newsfeed(){
        favouriteArticles = new String[10];
    }

    // allows user to add an article to a separate 'favourites' list
    public void setFavouriteArticle(int favouriteIndex, String newArticle){
        favouriteArticles[favouriteIndex] = newArticle;
    }

    // returns the list of topics
    public String[] getTopics(){
        return topics;
    }

    // gets the most viewed topic
    public String getTopTopic(){
        return topics[0];
    }

    // increments the number of views a topic has every time it is viewed
    public void viewTopic(int topicIndex){
        views[topicIndex] = views[topicIndex] + 1;
    }

    // returns the length of the topics array
    public int getNumTopics(){
        return topics.length;
    }

    public static void main(String[] args){
        Newsfeed sampleFeed = new Newsfeed();
        String[] topics = sampleFeed.getTopics();
        System.out.println(topics); // prints the memory address of the array.
        String printout = Arrays.toString(topics);
        System.out.println(printout); // prints the stringified array.
        System.out.println("The top topic is "+ sampleFeed.getTopTopic());
        sampleFeed.viewTopic(1);
        sampleFeed.viewTopic(1);
        sampleFeed.viewTopic(3);
        sampleFeed.viewTopic(2);
        sampleFeed.viewTopic(2);
        sampleFeed.viewTopic(1);
        System.out.println("The "+sampleFeed.topics[1]+" topic has been viewed "+sampleFeed.views[1]+" times!");
        sampleFeed.setFavouriteArticle(2, "Humans: Exterminate Or Not?");
        sampleFeed.setFavouriteArticle(3, "Organic Eye Implants");
        sampleFeed.setFavouriteArticle(0, "Oil News");
        System.out.println(Arrays.toString(sampleFeed.favouriteArticles));
        System.out.println("The number of topics is "+sampleFeed.getNumTopics());
    }

}
