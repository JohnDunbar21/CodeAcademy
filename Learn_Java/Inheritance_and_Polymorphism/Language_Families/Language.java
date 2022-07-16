package Learn_Java.Inheritance_and_Polymorphism.Language_Families;

public class Language {
    
    protected String name;
    protected int numSpeakers;
    protected String regionsSpoken;
    protected String wordOrder;

    Language(String langNme, int numSpeaker, String regionsUsed, String wordOrder){
        this.name = langNme;
        this.numSpeakers = numSpeaker;
        this.regionsSpoken = regionsUsed;
        this.wordOrder = wordOrder;
    }

    public void getInfo(){
        System.out.println(name+" is spoken by "+numSpeakers+" people mainly in"+regionsSpoken+".");
        System.out.println("The language follows the word order: "+wordOrder);
    }

    public static void main(String[] args){

        /*
        NOTICE: The information on the number of speakers is purely fictitious and does not intend to misrepresent official data in any way.
         */

        Language english = new Language("English", 123456789, "Europe and USA", "sub-vb-obj");
        english.getInfo();

        Mayan kiche = new Mayan("Ki'che'", 2330000);
        kiche.getInfo();

        SinoTibetan manChinese = new SinoTibetan("Mandarin Chinese", 57000000);
        SinoTibetan burmese = new SinoTibetan("Burmese", 34000000);
        manChinese.getInfo();
        burmese.getInfo();
    }
}
