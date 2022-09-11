package Learn_Intermediate_Java.Generics_and_Collections.LetsGetTakeout_Project;

public class Customer {
    private String name;
    private int money;
  
    public Customer(String name, int money) {
      this.name = name;
      this.money = money;
    }
  
    public String getName() {
      return this.name;
    }
  
    public int getMoney() {
      return this.money;
    }
  
    public void setMoney(int money) {
      this.money = money;
    }
  }