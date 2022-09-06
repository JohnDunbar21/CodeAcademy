package Learn_Intermediate_Java.Serialisation;

import java.io.Serializable;
import java.io.FileOutputStream;
import java.io.FileInputStream;
import java.io.ObjectOutputStream;
import java.io.ObjectInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;

/*
Although JVM implicitly serializes non-static fields, we can instruct the JVM to ignore them using the 'transient' keyword: this will have its value
ignored during serialization and instead receive the default value for that type of field.

Let’s discuss some interesting aspects of deserializing objects with transient and static fields:

    - The deserialize (copy) object will not get the default value for a static field (in our example the value 0), it will instead receive the 
      current value of the static field since program execution since static fields belong to the class and not the object.

    - A constructor is not called during deserialization for the deserialized type object. Object fields are set using reflection.

    - A constructor is only called for the first non-serializable class in the parent hierarchy of the deserialized object.

Most of the time we want to serialize all non-static fields in an object but you may find the need for transient fields if a field has its value 
generated based on other fields or, most importantly, if you have a reference field that is not serializable.
*/

public class Car4 implements Serializable {
  private String make;
  private int year;
  private static final long serialVersionUID = 1L;
  private transient String model; // the 'transient' keyword means JVM will not serialise that field.

  public Car4(String make, int year, String model) {
    this.make = make;
    this.year = year;
    this.model = model;
  }

  public String toString(){
    return String.format("Car make is: %s, Car year is: %d, Car model is: %s, serialVersionUID: %d", this.make, this.year, this.model, serialVersionUID);
  }

  public static void main(String[] args) throws FileNotFoundException, IOException, ClassNotFoundException {
    Car4 toyota = new Car4("Toyota", 2021, "Corolla");
    Car4 honda = new Car4("Honda", 2020, "Civic");
    FileOutputStream fileOutputStream = new FileOutputStream("cars.txt");
    ObjectOutputStream objectOutputStream = new ObjectOutputStream(fileOutputStream);
    objectOutputStream.writeObject(toyota);
    objectOutputStream.writeObject(honda);

    objectOutputStream.close();

    FileInputStream fileInputStream = new FileInputStream("cars.txt");
    ObjectInputStream objectInputStream = new ObjectInputStream(fileInputStream);

    Car4 toyotaCopy = (Car4) objectInputStream.readObject();
    //Car4 hondaCopy = (Car4) objectInputStream.readObject();

    objectInputStream.close();

    boolean isSameObject = toyotaCopy == toyota;
    System.out.println("Toyota (Copy) - "+ toyotaCopy);
    System.out.println("Toyota (Original) - "+ toyota);
    System.out.println("Is same object: "+ isSameObject);
  }
}