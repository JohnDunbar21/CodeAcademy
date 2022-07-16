package Learn_Java.Inheritance_and_Polymorphism.Language_Families;

public class Mayan extends Language{
    
    Mayan(String languageName, int speakers){
        super(languageName, speakers, "Central America", "vb-obj-sub");
    }

    @Override
    public void getInfo(){
        System.out.println(this.name+" is spoken by "+this.numSpeakers+" people mainly in the "+this.regionsSpoken+".");
        System.out.println("The language follows the word order: "+this.wordOrder);
        System.out.println("Fun fact: "+this.name+" is an ergative language.");
    }
}
