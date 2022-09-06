package Learn_Intermediate_Java.Serialisation;

import java.io.Serializable;

/*
In this example, the variable serialVersionUID acts as an identifier for the JVM to choose the proper class to convert a stream of bytes
back into an object.

Although JVM uses serialVersionUID to locate the proper class, it does not store the class file as part of the serialization.
*/

public class Car implements Serializable {
    /*
    private String make;
    private int year;
    */

    private static final long serialVersionUID = 1L; // 'long' type values must end with an 'L'
    

}
