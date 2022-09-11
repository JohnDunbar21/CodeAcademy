package Learn_Intermediate_Java.Generics_and_Collections.LetsGetTakeout_Project;

import java.util.ArrayList;
import java.util.List;

public class FoodMenu {
  private List<Food> menu = new ArrayList<>();

  public FoodMenu() {
    menu.add("Burger", "with cheese and salad", 12);
    menu.add("Hot Dog", "with caramelised onions", 10);
    menu.add("Pizza", "with custom toppings", 8);
  }

  // numbers have not been added to the method yet
  @ Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    for (Food item: menu) {
      sb.append(item.toString());
    }
    return sb.toString();
  }

  public Food getFood(int index) {
    if (index >= 1 && index < menu.size() + 1) {
      return menu.get(index);
    } else {
      return null;
    }
  }

  public Food getLowestCostFood() {
    int lowest = menu.get(0).getPrice(); // returns the price of index 1
    Food cheapest;
    for (Food item: menu) {
      if (item.getPrice() < lowest) {
        cheapest = item; // sets cheapest to the current lowest value
        lowest = item.getPrice(); // updates lowest to the new lowest value
      } else {
        continue;
      }
    }
    return cheapest;
  }
}