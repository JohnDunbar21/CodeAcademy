package Learn_Java.Object_Oriented_Java;

public class SavingsAccount_V2 {
    int balance;

    public SavingsAccount_V2(int initialBalance){
        balance = initialBalance;
    }

    public void checkBalance(){
        System.out.println("Hello!");
        System.out.println("Your balance is "+balance);
    }

    public void deposit(int amountToDeposit){
        int newBalance = balance + amountToDeposit;
        balance = newBalance;
        System.out.println("You just deposited "+amountToDeposit);
    }

    public int withdraw(int amountToWithdraw){
        int newBalance = balance - amountToWithdraw;
        balance = newBalance;
        System.out.println("You just withdrew "+amountToWithdraw);
        return amountToWithdraw;
    }

    public static void main(String[] args){
        SavingsAccount_V2 savings = new SavingsAccount_V2(2000);

        savings.checkBalance();
        savings.deposit(500);
        savings.checkBalance();
        savings.withdraw(200);
        savings.checkBalance();
    }
}
