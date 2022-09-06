package Learn_Intermediate_Java.Serialisation.CustomSerialization;

public class Engine {
    private double liters;
    private int cylinders;
  
    public Engine(double liters, int cylinders) {
      this.liters = liters;
      this.cylinders = cylinders;
    }
  
    public double getLiters() {
      return this.liters;
    }
  
    public int getCylinders() {
      return this.cylinders;
    }
  
    public String toString() {
      return String.format("Engine liters is: %f, Engine cylinders is: %d", this.liters, this.cylinders);
    }
  }