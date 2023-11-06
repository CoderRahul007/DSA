// If Class B is subtype of Class A , then we should be able to replace object of A with B without breaking the behaviour of program

// this means Sublass should extend the capability of parent class not narrow it down

interface Bike {
    void turnOnEngine();
    void accelerate();    
}

class Motorcycle implements Bike {
    // this is right
    boolean isEngineOn;
    int speed;
    public void turnOnEngine(){
        isEngineOn  = true
    }
    public void accelerate() {
        speed = speed + 10;
    }    
}

class Bicycle implements Bike {
    // This is wrong we are narrowing the capability
    public void turnOnEngine() {
        throw new AssertionError(detailMessage : "there is no engine");
    }

    public void accelerate(){

    }

}