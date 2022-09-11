package Learn_Intermediate_Java.Generics_and_Collections.LetsGetTakeout_Project;

public interface IntUserInputRetriever<T> {
    T produceOutputOnUserInput(int selection) throws IllegalArgumentException;
}