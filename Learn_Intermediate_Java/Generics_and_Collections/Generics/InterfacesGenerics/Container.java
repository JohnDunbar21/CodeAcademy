package Learn_Intermediate_Java.Generics_and_Collections.Generics.InterfacesGenerics;

public class Container<T> implements Retriever<T> {
    private T data;
  
    public Container(T data) {
      this.data = data;
    }
  
    public void setData(T data) {
      this.data = data;
    }
  
    public T getData() {
      return this.data;
    }
  
    @Override
    public T retrieveData() {
      return this.data;
    }
  }