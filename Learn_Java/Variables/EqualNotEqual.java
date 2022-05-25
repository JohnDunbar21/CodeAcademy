package Learn_Java.Variables;

public class EqualNotEqual {
    public static void main(String[] args) {
        int songsA = 9;
        int songsB = 9;
        int albumLengthA = 41;
        int albumLengthB = 53;
        boolean sameNumberOfSongs = songsA == songsB;
        boolean differentLength = albumLengthA != albumLengthB;
        System.out.println(sameNumberOfSongs);
        System.out.println(differentLength);
    }
}
