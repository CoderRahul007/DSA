// if we are going to add if condition for ever method for checking Null then it would make code redundant

public interface Vehicle {
    int getTankCapacity();
    int getSeatingCapacity();
}

public class Car implements Vehicle{
    public int getTankCapacity(){
        return 40;
    }
    public int getSeatingCapacity(){
        return 5;
    }
}

public class NullVehicle  implements Vehicle {
    public int getTankCapacity(){
        return 0;
    }
    public int getSeatingCapacity(){
        return 0;
    }
}

public class VehicleFactory {
    static Vehicle getVehicleObject(String typeOfVehicle){
        if("Car".equals(typeOfVehicle)){
            return new Car();
        }
        return new NullVehicle();
    }
}

public class Main {
    public static void main(){
        Vehicle vehicle = VehicleFactory.getVehicleObject("Bike");
        printVehicleDetails(vehicle);
    }
}

private static void printVehicleDetails(Vehicle vehicle){
    System.out.prnt(vehicle.getSeatingCapacity());
    System.out.prnt(vehicle.getTankCapacity());
}