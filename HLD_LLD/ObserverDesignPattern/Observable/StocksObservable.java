package ObserverDesignPattern;

public interface StocksObservable {
    public void add(NotificationAlertObserver observer);

    public void remove(NotificationAlertObserver observer);

    public void notifySubscribers();

    public int getStockCount();

    public void setStockCount(int newStockAdded);
}