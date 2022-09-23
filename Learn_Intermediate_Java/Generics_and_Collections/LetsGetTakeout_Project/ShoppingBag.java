package Learn_Intermediate_Java.Generics_and_Collections.LetsGetTakeout_Project;

import java.util.HashMap;
import java.util.Map;

public class ShoppingBag<T extends PricedItem<Integer>> {
  protected Map<T, Integer> shoppingBag = new HashMap<>();
  

  public ShoppingBag() {
    this.shoppingBag = new HashMap<>();
  }

  public void addItem(T item) {
    if (shoppingBag.containsKey(item)) {
      shoppingBag.put(item, shoppingBag.get(item) + 1);
    } else {
      shoppingBag.put(item, 1);
    }
  }

  public int getTotalPrice() {
    int sumTotal = 0;
    for (Map.Entry<T, Integer> element: shoppingBag.entrySet()) {
      sumTotal = sumTotal + element.getKey().getPrice() * element.getValue();
    }
    return sumTotal;
  }

  public Map<T, Integer> getMap() {
    return this.shoppingBag;
  }

  public void setMap(Map<T, Integer> map) {
    this.shoppingBag = map;
  }
}