package Learn_Intermediate_Java.Generics_and_Collections.LetsGetTakeout_Project;

public interface PricedItem<T extends Number> {
    T getPrice();
    void setPrice(T price);
}