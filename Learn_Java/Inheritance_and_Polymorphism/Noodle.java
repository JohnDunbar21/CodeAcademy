package Learn_Java.Inheritance_and_Polymorphism;

public class Noodle {
    
    protected double lengthInCentimeters;
    protected double widthInCentimeters;
    protected String shape;
    protected String ingredients;
    protected String texture = "brittle";

    Noodle(double lenInCent, double wthInCent, String shp, String ingr){
        this.lengthInCentimeters = lenInCent;
        this.widthInCentimeters = wthInCent;
        this.shape = shp;
        this.ingredients = ingr;
    }

    // the 'protected' keyword means that only children of the class can access the method.

    // the 'final' keyword means that the method cannot be changed.
    final protected boolean isTasty(){
        return true;
    }

    public String getCookPrep(){
        return "Boil noodle for 7 minutes and add sauce";
    }

    public void cook(){
        this.texture = "cooked";
    }

    /* 
    public static void main(String[] args){
        Spaghetti spaghettiPomodoro = new Spaghetti();
        System.out.println(spaghettiPomodoro.texture);

        Pho phoChay = new Pho();
        System.out.println(phoChay.shape);

        Ramen yasaiRamen = new Ramen();
        System.out.println(yasaiRamen.isTasty());
        System.out.println(yasaiRamen.ingredients);

        Spaetzle kaesespaetzle = new Spaetzle();
        kaesespaetzle.cook();

        Noodle spaghetti, ramen, pho;

        spaghetti = new Spaghetti();
        ramen = new Ramen();
        pho = new Pho();

        Noodle[] allTheNoodles = {spaghetti, ramen, pho};

        for (Noodle noodle : allTheNoodles){
            System.out.println(noodle.getCookPrep());
        }
    }
    */
    
}

class NoodleRestaurant{
    String name;

    public NoodleRestaurant(String customerName){
        name = customerName;
    }

    public void order(Noodle noodle){
        System.out.println(noodle.getCookPrep());
        System.out.println("Order for "+name+" is ready.");
    }

    public static void main(String[] args){
        Noodle ramen, pho;
        ramen = new Ramen();
        pho = new Pho();

        NoodleRestaurant customer1 = new NoodleRestaurant("Jasper");
        NoodleRestaurant customer2 = new NoodleRestaurant("Martha");

        customer1.order(pho);
        customer2.order(ramen);
    }
}

class Spaetzle extends Noodle{
    
    Spaetzle() {
    
        super(3.0, 1.5, "irregular", "eggs, flour, salt");
        this.texture = "lumpy and liquid";
        
      }


    // the '@Override' keyword assists in polymorphism by specifying to the compiler that the method is being changed, but has the same name
    @Override
    public void cook(){
        System.out.println("Grinding or scraping dough.");
        System.out.println("Boiling");
        this.texture = "cooked";
    }
      
}

class BiangBiang extends Noodle{

    BiangBiang(){
        super(50.0, 5.0, "flat", "high-gluten flour, salt, water");
    }
}

class Dinner {

    /*
    private void makeNoodles(Noodle noodle, String sauce){

        noodle.cook();

        System.out.println("Mixing "+ noodle.texture +" noodles made from "+ noodle.ingredients +" with "+ sauce +".");
        System.out.println("Dinner is served!");
    }

     
    public static void main(String[] args){

        Dinner noodlesDinner = new Dinner();
        Noodle biangBiang = new BiangBiang();
        noodlesDinner.makeNoodles(biangBiang, "soy sauce and chilli oil");
    }
    */
}