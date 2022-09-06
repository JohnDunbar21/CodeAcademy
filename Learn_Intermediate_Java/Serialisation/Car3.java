package Learn_Intermediate_Java.Serialisation;

import java.io.Serializable;
import java.io.FileOutputStream;
import java.io.FileInputStream;
import java.io.ObjectOutputStream;
import java.io.ObjectInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;

/*
When deserializing an a file to an object, we need to use the helper classes 'FileInputStream' and 'ObjectInputStream' as shown below.
We then use the 'readObject' command to deserialize objects in our class.
*/

public class Car3 implements Serializable {
  private String make;
  private int year;
  private static final long serialVersionUID = 1L;

  public Car3(String make, int year) {
    this.make = make;
    this.year = year;
  }

  public String toString(){
    return String.format("Car make is: %s, Car year is: %d", this.make, this.year);
  }

  public static void main(String[] args) throws FileNotFoundException, IOException, ClassNotFoundException {
    Car3 toyota = new Car3("Toyota", 2021);
    Car3 honda = new Car3("Honda", 2020);
    FileOutputStream fileOutputStream = new FileOutputStream("cars.txt");
    ObjectOutputStream objectOutputStream = new ObjectOutputStream(fileOutputStream);
    objectOutputStream.writeObject(toyota);
    objectOutputStream.writeObject(honda);

    objectOutputStream.close();

    FileInputStream fileInputStream = new FileInputStream("cars.txt");
    ObjectInputStream objectInputStream = new ObjectInputStream(fileInputStream);

    Car3 toyotaCopy = (Car3) objectInputStream.readObject();
    //Car3 hondaCopy = (Car3) objectInputStream.readObject();

    objectInputStream.close();

    boolean isSameObject = toyotaCopy == toyota;

    System.out.println("Toyota (Copy) - "+toyotaCopy);
    System.out.println("Toyota (Original) - "+toyota);
    System.out.println("Is same object: "+isSameObject);
  }
}