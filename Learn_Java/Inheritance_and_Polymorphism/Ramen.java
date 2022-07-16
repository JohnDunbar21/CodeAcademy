package Learn_Java.Inheritance_and_Polymorphism;

public class Ramen extends Noodle{
    
    Ramen(){
        super(30.0, 0.3, "flat", "wheat flour");
    }

    //public boolean isTasty(){
        //return false;
    //}
    // a method with the same name as the parent will override it unless the parent's method has the 'final' keyword before the method

    @Override
    public String getCookPrep() {
      
      return "Boil ramen for 5 minutes in broth, then add meat, mushrooms, egg, and vegetables.";
      
    }
}
