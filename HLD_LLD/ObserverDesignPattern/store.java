package ObserverDesignPattern.Observer;

public class store {
    public static void main() {
        StockObservable iphoneStockObserable = new IphoneObservableImpl();

        NotificationAlertObserver observer1 = new EmailAlertObserverImpl("zyx@gmail.com", iphoneStockObserable);
        NotificationAlertObserver observer2 = new EmailAlertObserverImpl("zyx2@gmail.com", iphoneStockObserable);

        iphoneStockObserable.add(observer1);
        iphoneStockObserable.add(observer2);

        iphoneStockObserable.setStockCount(10);


    }
}
