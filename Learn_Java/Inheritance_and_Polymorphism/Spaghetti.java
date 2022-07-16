package Learn_Java.Inheritance_and_Polymorphism;

public class Spaghetti extends Noodle{
    // empty child class

    Spaghetti(){
        super(2.1, 3.2, "Round", "Dough");
    }

    @Override
    public String getCookPrep() {
      
      return "Boil spaghetti for 8 - 12 minutes and add sauce, cheese, or oil and garlic.";
      
    }
}
