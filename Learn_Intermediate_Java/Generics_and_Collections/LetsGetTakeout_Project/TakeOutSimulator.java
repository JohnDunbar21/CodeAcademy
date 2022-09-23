package Learn_Intermediate_Java.Generics_and_Collections.LetsGetTakeout_Project;

import java.util.Scanner;

public class TakeOutSimulator {
  private Customer customer;
  private FoodMenu menu;
  private Scanner input;

  public TakeOutSimulator(Customer customer, Scanner input) {
    this.customer = customer;
    this.input = input;
    this.menu = new FoodMenu(); // this could be wrong
  }

  private <T> T getOutputOnIntInput(String userInputPrompt, IntUserInputRetriever<T> intUserInputRetriever) {
    if (input.hasNextInt() == true) {
      System.out.println(userInputPrompt);
      int userInput = input.nextInt();
      try {
        return (T) intUserInputRetriever.produceOutputOnUserInput(userInput);
      } catch (IllegalArgumentException e) {
        System.out.println(userInput+" is not a valid input");
      }
    } else {
      System.out.println("Your input must be an integer");
    }
    return null;
  }

  public boolean shouldSimulate() {
    String userPrompt = "Enter 1 to CONTINUE simulation or 0 to EXIT program: \n";

    IntUserInputRetriever<?> intUserInputRetriever = (userChoice) -> {
      if (userChoice == 1 && customer.getMoney() >= menu.getLowestCostFood().getPrice()) {
        System.out.printf("Your choice was %s to continue, and you have enough money to complete the transaction.%n", userChoice);
        return true;
      } else if (userChoice == 1 && customer.getMoney() < menu.getLowestCostFood().getPrice()) {
        System.out.printf("Your choice was %s, but you do not have enough money to complete the transaction.\n", userChoice);
        System.out.println("ENDING SIMULATION");
        return false;
      } else if (userChoice == 0) {
        System.out.printf("You have chosen %s. SIMULATION ENDING", userChoice);
        return false;
      } else {
        throw new IllegalArgumentException("You have chosen an invalid selection. Try again.\n");
      }
    };
    return (boolean) getOutputOnIntInput(userPrompt, intUserInputRetriever);
  }

  public Food getMenuSelection() {
    String userPrompt = "Choose an item from the menu (answer using an integer): \n"+menu.toString();
    
    IntUserInputRetriever<?> intUserInputRetriever = (selection) -> {
      if (selection <= menu.menu.size()) {
        return menu.getFood(selection);
      } else {
        throw new IllegalArgumentException("You have made an invalid selection. Try again.\n"); 
      }
    };
    return (Food) getOutputOnIntInput(userPrompt, intUserInputRetriever);
  }

  public boolean isStillOrderingFood() {
    String userPrompt = "Enter 1 to CONTINUE shopping or 0 to CHECKOUT: ";

    IntUserInputRetriever<?> intUserInputRetriever = (choice) -> {
      if (choice == 1) {
        return true;
      } else if (choice == 0) {
        return false;
      } else {
        throw new IllegalArgumentException("You have made an invalid selection. Try again.\n");
      }
    };
    return (boolean) getOutputOnIntInput(userPrompt, intUserInputRetriever);
  }

  public void checkoutCustomer(ShoppingBag<Food> shoppingBag) {
    System.out.println("Processing payment...");
    int remainingMoney = customer.getMoney() - shoppingBag.getTotalPrice();
    customer.setMoney(remainingMoney);
    System.out.printf("Your remaining balance is: $%s",remainingMoney);
    System.out.println("Thank you for ordering with us, and enjoy your food.");
  }

  public void takeOutPrompt() {
    ShoppingBag<Food> shoppingBag = new ShoppingBag<Food>(); // unsure if this is correct
    int customerMoneyLeft = customer.getMoney();
    System.out.printf("You have $%s left to spend.", customerMoneyLeft);
    getMenuSelection();
    if (getMenuSelection().getPrice() <= customerMoneyLeft) {
      shoppingBag.shoppingBag.put(getMenuSelection());
      customerMoneyLeft -= getMenuSelection().getPrice();
    } else if (getMenuSelection().getPrice() >= customerMoneyLeft) {
      System.out.println("It looks like you cannot afford that item. Choose another item or checkout.");
      isStillOrderingFood();
      if (isStillOrderingFood() == true) {
        getMenuSelection();
      } else {
        break;
      }
        
    }
  }

  public void startTakeOutSimulator() {
    System.out.println("Welcome to my restaurant!");
    System.out.printf("Hello, %s!", customer.getName());
  }

}