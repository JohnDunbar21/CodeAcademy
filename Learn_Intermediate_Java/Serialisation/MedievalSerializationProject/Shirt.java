package Learn_Intermediate_Java.Serialisation.MedievalSerializationProject;

//import java.io.Serializable;

public class Shirt extends Armour {

  /* Class Variables */
  private static final long serialVersionUID = 1L;

  /* Constructors */
  public Shirt(String name, int durability, int defenseRating) {
    super(name, durability, defenseRating);
  }
}