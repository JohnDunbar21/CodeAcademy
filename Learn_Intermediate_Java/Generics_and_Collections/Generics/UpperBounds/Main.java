package Learn_Intermediate_Java.Generics_and_Collections.Generics.UpperBounds;

public class Main {
    public static void main(String[] args) {
      SchoolPerson person = new SchoolPerson("Peter");
      Bus<SchoolPerson> busWPerson = new Bus<>(person);
      busWPerson.printRider();    
    }
  }