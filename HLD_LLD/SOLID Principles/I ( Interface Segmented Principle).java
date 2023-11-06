// Interface should be such that client should not implement unnecessary functions they dont need
// means interface should contain features which are of their concern

// Wrong interface
interface RestaurantEmployee {
    void washDishers();
    void serverCustomers();
    void cookFood();
}


// Here Waiter class has to implement unnecesary functions
class Waiter implements RestaurantEmployee {
    public void washDishers(){
        // not his job
    }

    public void serverCustomers(){
        // his job
    }

    public void cookFood() {
        // not his job
    }
}


-------------------------------------------------

interface WaiterInterface {
    void serverCustomers();
    void takeOrders();    
}

interface ChefInterface {
    void cookFood();
    void decideMenu();
}

class Waiter implements WaiterInterface {   

    public void serverCustomers(){
        // his job
    }

    public void takeOrders() {
        //  his job
    }
}