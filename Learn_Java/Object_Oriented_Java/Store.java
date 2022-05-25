package Learn_Java.Object_Oriented_Java;

public class Store {
    String productType;
    int inventoryCount;
    double inventoryPrice;

    public Store(String product, int count, double price) {
        productType = product;
        inventoryCount = count;
        inventoryPrice = price;
    }
    public static void main(String[] args) {
        System.out.println("Start of the main method.");
        Store cookieShop = new Store("cookies", 12, 3.75);
        System.out.println(cookieShop);
    }
}
