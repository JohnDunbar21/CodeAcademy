package Learn_Intermediate_Java.Serialisation;

import java.io.Serializable;
import java.io.FileOutputStream;
import java.io.ObjectOutputStream;
import java.io.FileNotFoundException;
import java.io.IOException;

// the class variables and constructor variables have been commented out to prevent 'variable not accessed' error being thrown as VSC seems to have an issue.

/*
When serializing an object to a file, we need to use the helper classes 'FileOutputStream' and 'ObjectOutputStream' as shown below.
We then use the 'writeObject' command to serialize objects in our class.
*/

public class Car2 implements Serializable {
  //private String make;
  //private int year;
  private static final long serialVersionUID = 1L;

  public Car2(String make, int year) {
    //this.make = make;
    //this.year = year;
  }

  public static void main(String[] args) throws FileNotFoundException, IOException {

    Car2 toyota = new Car2("Toyota", 2021);
    Car2 honda = new Car2("Honda", 2020);

    FileOutputStream fileOutputStream = new FileOutputStream("cars.txt");
    ObjectOutputStream objectOutputStream = new ObjectOutputStream(fileOutputStream);

    objectOutputStream.writeObject(toyota);
    objectOutputStream.writeObject(honda);

    objectOutputStream.close();
  }
}