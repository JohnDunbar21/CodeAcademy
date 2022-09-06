package Learn_Intermediate_Java.Serialisation.MedievalSerializationProject;

//import java.io.Serializable;

public class Helmet extends Armour  {

  /* Class Variables */
  private static final long serialVersionUID = 1L;

  /* Constructors */
  public Helmet(String name, int durability, int defenseRating) {
    super(name, durability, defenseRating);
  }
}