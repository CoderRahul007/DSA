// Class should depend on interfaces rather than concrete classes


// wrong
class Macbook {
    private final Wiredkeyboard keyboard;
    private final WiredMouse mouse;
    public Macbook() {
        keyboard = new Wiredkeyboard(); // we are using concrete classes objects
        mouse = new WiredMouse();        
    }
}


// Right
class Macbook {
    private final Keyboard keyboard;
    private final Mouse mouse;
    public Macbook(Keyboard keyboard , Mouse mouse) {
        this.keyboard = keyboard;
        this.mouse = mouse;
              
    }
}