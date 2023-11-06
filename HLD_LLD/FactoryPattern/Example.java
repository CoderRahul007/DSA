// When we want to create Object based on some conditions then we use the Factory design patterrn

public interface Shape {
    public void draw();
}

public class Circle {
    // is a relationship to Shape
    public void draw(){
        // draws the circle
    }
}

public class Square {
    // is a relationship to Shape
    public void draw(){
        // draws the square
    }
}


public class ShapeFactory {
    // has a relationship to Shape
    Shape shape;
    public Shape getShape(String input){
        // based on condition return the shape object
    }
}

////////////////////////////////////////////////////////////////////////

// Abstract Factory Design pattern means Factory of factory classes
// When we want to group the variuous classes according to factories
// take example of LuxuryCar Factory , SportsCarFactor etc