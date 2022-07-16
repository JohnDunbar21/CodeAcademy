package Learn_Java.Inheritance_and_Polymorphism.Language_Families;

public class SinoTibetan extends Language{
    
    SinoTibetan(String langName, int speakers){
        super(langName, speakers, "Asia", "sub-obj-vb");

        if (langName.contains("Chinese")){
            this.wordOrder = "sub-vb-obj";
        }
    }
}
