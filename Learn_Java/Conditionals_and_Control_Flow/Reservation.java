package Learn_Java.Conditionals_and_Control_Flow;

public class Reservation {
    int guestCount;
    int restaurantCapacity;
    boolean isRestaurantOpen;
    boolean isConfirmed;

    // class constructor
    public Reservation(int count, int capacity, boolean open){
        if (count <= 0 || count > 8){
            System.out.println("Invalid reservation!");
        }
        guestCount = count;
        restaurantCapacity = capacity;
        isRestaurantOpen = open;
    }

    // reservation method
    public void confirmReservation(){
        if (restaurantCapacity >= guestCount && isRestaurantOpen == true) {
            System.out.println("Reservation confirmed");
            isConfirmed = true;
        } else {
            System.out.println("Reservation denied");
            isConfirmed = false;
        }
    }

    // confirmation of action to user
    public void informUser(){
        if (!isConfirmed){
            System.out.println("Unable to confirm reservation. Please contact the restaurant directly to assist with your booking.");
        } else {
            System.out.println("Please enjoy your meal!");
        }
    }

    public static void main(String[] args){
        Reservation partyOfThree = new Reservation(3, 12, true);
        Reservation partyOfFour = new Reservation(4, 3, true);
        partyOfThree.confirmReservation();
        partyOfThree.informUser();
        partyOfFour.confirmReservation();
        partyOfFour.informUser();
    }
}
