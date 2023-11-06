// A class should have only 1 reason to change
class Marker {
    String name;
    String color;
    int price;

    public Marker(String name , String color , int price){
        this.name = name;
        this.color = color;
        this.price = price;

    }
}

// Invoice has a relationship with the Marker

class Invoice {
    private Marker marker;
    private int quantity;

    public Invoice(Marker marker , int quantity){
        this.marker = marker;
        this.quantity = quantity;
    }

    public int calculateTotal() {
        int price = ((marker.price) * this.quantity);
        return price;
    }

    public void printInvoice(){

    }

    public void saveToDb(){

    }
}

// Invoice class doesnt follow S(SRP) , it is being changed when logic change in savetoDb , printInvoice  , calculateTotal



class Invoice {
    private Marker marker;
    private int quantity;

    public Invoice(Marker marker , int quantity){
        this.marker = marker;
        this.quantity = quantity;
    }

    public int calculateTotal() {
        int price = ((marker.price) * this.quantity);
        return price;
    }

}

class InvoiceDao{
    private Invoice invoice;
    public InvoiceDao(Invoice invoice) {
        this.invoice = invoice;
    }

    public void saveToDb(){

    }
}

class InvoicePrinter {
    private Invoice invoice;
    public InvoicePrinter( Invoice invoice ){
        this.invoice  = invoice;
    }

    public void print(){

    }
}

// Now it follows SRP
