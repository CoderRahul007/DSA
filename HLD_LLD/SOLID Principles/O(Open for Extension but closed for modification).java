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

// the below dao is already tested but i have added another method which may have bugs
class InvoiceDao{
    private Invoice invoice;
    public InvoiceDao(Invoice invoice) {
        this.invoice = invoice;
    }

    public void saveToDb(){

    }

    public void saveToFile(String filename){

    }
}


----------------------------------------------------------

// Here we will implement another class for the invoice
interface InvoiceDao {
    public void save(Invoice invoice);
}


class DatabaseDao implements InvoiceDao {
    @Override
    public void save(Invoice invoice) {
        // save to Db
    }
}

class FileInvoiceDao implements InvoiceDao {
    @Override
    public void save(Invoice invoice) {
        // save to File 
    }
}

