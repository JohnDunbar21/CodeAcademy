package Learn_Java.Object_Oriented_Java;

public class Droid {
    /*
    A company is missing some instructions to help create robots and what they will do.
    Write a Java class to help.
    */
    
    String name;
    int batteryLevel;

    public Droid(String droidName){
        name = droidName;
        batteryLevel = 100;
    }

    public String toString(){
        return "Hello, I'm the droid: "+name;
    }

    public void performTask(String task){
        System.out.println(name+" is performing task: "+task);
        int newBatteryLevel = batteryLevel - 10;
        batteryLevel = newBatteryLevel;
    }

    public String energyReport(){
        return name+" has a battery level of: "+batteryLevel+"%";
    }

    public static void main(String[] args){
        Droid codey = new Droid("Codey");
        System.out.println(codey.toString());
        codey.performTask("Dancing");
        System.out.println(codey.energyReport());
        codey.performTask("Running");
        System.out.println(codey.energyReport());
    }
}
