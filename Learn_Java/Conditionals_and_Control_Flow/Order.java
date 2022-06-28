package Learn_Java.Conditionals_and_Control_Flow;

public class Order {
    boolean isFilled;
    double billAmount;
    String shipping;
    String couponCode;
    
    public Order(boolean filled, double cost, String shippingMethod, String coupon){
        if (cost > 24.00){
            System.out.println("High value item!");
        } else {
            System.out.println("Low value item!");
        }
        isFilled = filled;
        billAmount = cost;
        shipping = shippingMethod;
        couponCode = coupon;
    }

    public void ship(){
        if (isFilled){
            System.out.println("Shipping");
            System.out.println("Shipping cost: "+calculateShipping());
        } else {
            System.out.println("Order not ready");
        }
    }
    public double calculateShipping(){
        // Switch statement replaced if-then-else statements.
        /*if (shipping == "Regular"){
            return 0;
        } else if (shipping == "Express"){
            //return 1.75;
            if (couponCode == "ship50"){
                return 0.85;
            } else{
                return 1.75;
            }
        } else {
            return 0.5;
        }*/
        double shippingCost;

        switch(shipping){
            case "Regular":
                shippingCost = 0;
                break;
            case "Express":
                if (couponCode == "ship50") {
                    shippingCost = 0.85;
                } else {
                    shippingCost = 1.75;
                }
                break;
            default:
            shippingCost = 0.5;
        }

        return shippingCost;
    }

    public static void main(String[] args){
        Order book = new Order(true, 9.99, "Express", "ship50");
        Order chemistrySet = new Order(false, 72.50, "Regular", "freeShipping");
        book.ship();
        chemistrySet.ship();
    }
}
