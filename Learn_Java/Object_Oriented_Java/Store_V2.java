package Learn_Java.Object_Oriented_Java;

public class Store_V2 {
    // instance fields
    String productType;
    double price;

    // constructor method
    public Store_V2(String product, double initialPrice) {
        productType = product;
        price = initialPrice;
    }

    // advertise method
    public void advertise() {
        System.out.println("Come spend some money!");
        System.out.println("Selling " +productType +"!");
    }

    // greet customer method
    public void greetCustomer(String customer) {
        System.out.println("Welcome to the store, " +customer +"!");
    }

    // price increase method
    public void increasePrice(double priceToAdd) {
        double newPrice = price + priceToAdd;
        price = newPrice;
    }

    // get price with tax method
    public double getPriceWithTax() {
        double totalPrice = price + price * 0.08;
        return totalPrice;
    }

    // toString methods describing each store
    public String toString() {
        return "This store sells "+productType+" at a price of "+price+".";
    }

    // main method
    public static void main (String[] args) {
        Store_V2 lemonadeStand = new Store_V2("Lemonade", 3.75);
        lemonadeStand.advertise();
        lemonadeStand.greetCustomer("Bartholemew");
        lemonadeStand.increasePrice(1.5);
        System.out.println(lemonadeStand.price);
        double lemonadePrice = lemonadeStand.getPriceWithTax();
        System.out.println(lemonadePrice);
        System.out.println(lemonadeStand); // this will print a string with productType and price instead of the object's location in memory.
        
    }
}
