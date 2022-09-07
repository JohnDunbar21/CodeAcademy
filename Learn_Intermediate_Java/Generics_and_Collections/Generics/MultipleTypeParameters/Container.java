package Learn_Intermediate_Java.Generics_and_Collections.Generics.MultipleTypeParameters;

public class Container<T, S> {
    private T item1;
    private S item2;
  
    public Container(T item1, S item2) {
      this.item1 = item1;
      this.item2 = item2;
    }
  
    public T getItem1() {
      return this.item1;
    }
  
    public S getItem2() {
      return this.item2;
    }
  }