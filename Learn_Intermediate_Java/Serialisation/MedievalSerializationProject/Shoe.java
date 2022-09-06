package Learn_Intermediate_Java.Serialisation.MedievalSerializationProject;

//import java.io.Serializable;

public class Shoe extends Armour {

  /* Class Variables */
  private static final long serialVersionUID = 1L;

  /* Constructors */
  public Shoe(String name, int durability, int defenseRating) {
    super(name, durability, defenseRating);
  }
}