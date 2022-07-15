package Learn_Java.Access_Encapsulation_and_Static_Methods;

// the 'this' keyword can set a local variable to the instance variable

public class SavingsAccount {
    
    public String owner;
    public int balanceDollar;
    public double balanceEuro;
  
    public SavingsAccount(String owner, int balanceDollar){
      // Complete the constructor
      this.owner = owner;
      this.balanceDollar = balanceDollar;
      this.balanceEuro = balanceDollar * 0.85;
    }
  
    public void addMoney(int balanceDollar){
      // Complete this method
      System.out.println("Adding "+balanceDollar+" dollars to the account.");
      this.balanceDollar = this.balanceDollar + balanceDollar;
      System.out.println("The new balance is "+this.balanceDollar+" dollars.");
    }
  
    public static void main(String[] args){
      SavingsAccount zeusSavingsAccount = new SavingsAccount("Zeus", 1000);
  
      // Make a call to addMoney() to test your method
      zeusSavingsAccount.addMoney(2000);
    }
}
