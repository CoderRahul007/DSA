class Vehicle {
    public void drive();
}

class SportVehicle extends Vehicle{
    @Override
    public void drive(){
        // special capacity same for offroad and sport
    }    
}

class PassengerVehicle extends Vehicle{
    super.drive() // use the same as Vehicle class
}

class OffRoadVehicle extends Vehicle{
    @Override
    public void drive(){
        // special capacity same for offroad and sport
    }
}

// In the above example OffRoad and Sporty are using same method implementation which is duplicating the code
// to avoid that


// Correct Implementation

interface DriveStrategy {
    public void drive();
}

class NormalDrive implements DriveStrategy {
    public void drive();
}

class SpecialDrive implements DriveStrategy {
    public void drive();
}


class Vehicle {
    DriveStrategy obj; 
    public Vehicle(DriveStrategy obj) {
        this.obj = obj
    }
    public void drive(){
        obj.drive();
    }
}

class SportVehicle extends Vehicle{
    public SportVehicle() {
        super(new SpecialDrive())
    }
}

public class Main {
    public static void main(){
        Vehicle vehicle = new SportVehicle();
        vehicle.drive();
    }
}