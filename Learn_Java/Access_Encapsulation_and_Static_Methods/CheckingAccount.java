package Learn_Java.Access_Encapsulation_and_Static_Methods;

public class CheckingAccount {
    private String name;
    private int balance;
    private double interestRate;
  
    public CheckingAccount(String inputName, int inputBalance){
      this.name = inputName;
      this.balance = inputBalance;
      this.interestRate = 0.02;
    }
    
    // should be private if not used with the Bank.java file
    public void addFunds(int fundsToAdd){
      balance += fundsToAdd;
    }
  
    // should be private if not used with the Bank.java file
    public void getInfo(){
      System.out.println("This checking account belongs to " + name +". It has " + balance + " dollars in it.");
    }

    public int getBalance(){
        return balance;
    }

    public String getName(){
        return name;
    }

    public void setBalance(int newBalance){
        balance = newBalance;
    }

    private double calculateNextMonthInterest(){
      return this.balance * this.interestRate;
    }

    public void getAccountInformation(){
      System.out.println("Current balance in account: "+this.getBalance());
      System.out.println("Next month's interest: "+this.calculateNextMonthInterest());
    }

    public static void main(String[] args){
        CheckingAccount myAccount = new CheckingAccount("John", 5000);
        System.out.println(myAccount.balance);
        myAccount.addFunds(5);
        System.out.println(myAccount.balance);
    }
}
