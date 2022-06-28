package Learn_Java.Conditionals_and_Control_Flow;

public class CarLoan {

    public static void main(String[] args){

        int carLoan = 10000; // represents the value of the product in units of currency.
        int loanLength = 3; // represents 3 years.
        int interestRate = 5; // represents the annual interest rate.
        int downPayment = 2000; // represents the customer downpayment in units of currency.

        if (loanLength <= 0){
            System.out.println("There seems to be an error in the loan duration: please select a valid loan length.");
        } else if (downPayment >= carLoan){
            System.out.println("Based on the amount you have assigned for a downpayment, you are eligible to pay for the car outright.");
        } else {
            int remainingBalance = carLoan - downPayment;
            int months = loanLength * 12;
            int monthlyBalance = remainingBalance / months;
            int interest = (monthlyBalance * interestRate) / 100;
            int monthlyPayment = monthlyBalance + interest;
            System.out.println(monthlyPayment);
        }

    }
}
