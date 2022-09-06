package Learn_Intermediate_Java.Serialisation.SerializingAssociatedFields;

import java.io.Serializable;
public class Engine implements Serializable{
  private double liters;
  private int cylinders;

  public Engine(double liters, int cylinders){
    this.liters = liters;
    this.cylinders = cylinders;
  }

  public String toString(){
    return String.format("Engine liters is:%f, Engine cyclinders is: %d", this.liters, this.cylinders);
  }
}