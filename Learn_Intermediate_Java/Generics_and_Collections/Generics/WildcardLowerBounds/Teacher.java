package Learn_Intermediate_Java.Generics_and_Collections.Generics.WildcardLowerBounds;

public class Teacher extends SchoolPerson {
    private String subject;
  
    public Teacher(String name, String subject) {
      super(name);
      this.subject = subject;
    }
  
    public void setSubject(String subject) {
      this.subject = subject;
    }
  
    public String getSubject() {
      return this.subject;
    }
  
    public String toString() {
      return "Teacher = (name = "+this.getName()+", subject = "+ this.subject+")";
    }
  }