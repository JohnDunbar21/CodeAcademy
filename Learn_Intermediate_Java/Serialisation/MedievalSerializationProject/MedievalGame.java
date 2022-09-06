package Learn_Intermediate_Java.Serialisation.MedievalSerializationProject;

import java.util.Scanner;
import java.util.Objects;
import java.io.FileOutputStream;
import java.io.ObjectOutputStream;
import java.io.IOException;
import java.io.FileInputStream;
import java.io.ObjectInputStream;

public class MedievalGame {

  /* Instance Variables */
  private Player player;

  /* Main Method */
  public static void main(String[] args) {
    
    Scanner console = new Scanner(System.in);
    MedievalGame game = new MedievalGame();

    game.player = game.start(console);

    game.addDelay(500);
    System.out.println("\nLet's take a quick look at you to make sure you're ready to head out the door.");
    System.out.println(game.player);

    game.addDelay(1000);
    System.out.println("\nWell, you're off to a good start, let's get your game saved so we don't lose it.");
    game.save();

    game.addDelay(2000);
    System.out.println("We just saved your game...");
    System.out.println("Now we are going to try to load your character to make sure the save worked...");

    game.addDelay(1000);
    System.out.println("Deleting character...");
    String charName = game.player.getName();
    game.player = null;

    game.addDelay(1500);
    game.player = game.load(charName, console);
    System.out.println("Loading character...");

    game.addDelay(2000);
    System.out.println("Now let's print out your character again to make sure everything loaded:");

    game.addDelay(500);
    System.out.println(game.player);
  } // End of main

  /* Instance Methods */
  private Player start(Scanner console) {
    // Add start functionality here
    Player player;
    Art.homeScreen();
    System.out.println("Welcome Traveler, you have come a long way!");
    System.out.println("To load a game, enter 'y'.");
    System.out.println("To start a new game, enter 'n'.");
    String answer = console.next().toLowerCase();
    while (true) {
      if (answer.equals("y")) {
        System.out.println("");
        System.out.println("I thought I recognised your face! If you tell me your name, I'll go and get your things.");
        player = load(console.next(), console);
        break;
      } else if (answer.equals("n")) {
        System.out.println("");
        System.out.println("I see, so you're new around here, huh? Well, tell me your name!");
        String userName = console.next();
        while (true) {
          System.out.println("Welcome "+userName+", correct me if I am mispronouncing it. Enter 'y' to confirm, or 'n' to restart.");
          String nameConfirm = console.next().toLowerCase();
          if (Objects.equals(nameConfirm, "y")) break;
          System.out.println("I am terribly sorry, but I did not quite get that. Could you tell me your name again?");
          userName = console.next();
        }
        player = new Player(userName);
        break;
      } else {
        System.out.println("You chose an invalid option, Traveler. Please choose either 'y' to load a game, or 'n' to start a new one!");
        answer = console.next().toLowerCase();
      }
    }

    return player;
  } // End of start

  private void save() {
    // Add save functionality here
    String filename = player.getName() + ".svr";
    try {
      FileOutputStream userSave = new FileOutputStream(filename);
      ObjectOutputStream playerSave = new ObjectOutputStream(userSave);

      playerSave.writeObject(this.player);

      playerSave.close();
    } catch (IOException e) {
      System.out.println("An error occured while saving your file...");
    }
  } // End of save

  private Player load(String playerName, Scanner console) {
    // Add load functionality here
    Player loadedPlayer;
    try {
      FileInputStream userLoad = new FileInputStream(playerName + ".svr");
      ObjectInputStream playerLoad = new ObjectInputStream(userLoad);

      loadedPlayer = (Player) playerLoad.readObject();

      playerLoad.close();
    } catch (IOException | ClassNotFoundException e) {
      addDelay(1500);
      System.out.println("There has been an error loading your saved file...");
      addDelay(2000);
      loadedPlayer = new Player(playerName);
    }

    return loadedPlayer;
  } // End of load

  // Adds a delay to the console so it seems like the computer is "thinking"
  // or "responding" like a human, not instantly like a computer.
  private void addDelay(int time) {
    try {
      Thread.sleep(time);
    } catch (InterruptedException e) {
      e.printStackTrace();
    }
  }
}