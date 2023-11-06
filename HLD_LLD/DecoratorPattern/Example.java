// This pattern solves Class Explosion

public abstract class  BasePizza {
    public abstract int cost();
}

public class FarmHouse extends BasePizza {
    @Override
    public int cost(){
        return 200;
    }
}

public class VegDelight extends BasePizza {
    @Override
    public int cost() {
        return 120;
    }

}

public class Margherita extends BasePizza {
    @Override
    public int cost(){
        return 100;
    }
}


public abstract class ToppingDecorator extends BasePizza {    
}

public class Extracheese extends ToppingDecorator {
    BasePizza basePizza ;
    public Extracheese(BasePizza basePizza) {
        this.basePizza = basePizza;
    }

    @Override
    public int cost(){
        return this.basePizza.cost() + 50
    }
}


// Suppose we want Margherita + Extracheese

BasePizza pizza = new Extracheese(new Margherita())

