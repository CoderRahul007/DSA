package ObserverDesignPattern.Observable;

import ObserverDesignPattern.Observer.NotificationAlertObserver;

import java.util.ArrayList;
import java.util.List;

public class IphoneObservableImp implements StocksObservable {
    public List<NotificationAlertObserver> observerList = new ArrayList<>();
    public int stockCount = 0;

    public void add(NotificationAlertObserver observer) {
        observerList.add(observer);
    }

    public void remove(NotificationAlertObserver observer) {
        observerList.remove(observer);
    }

    public void notifySubscribers() {
        for (NotificationAlertObserver observer : observerList) {
            observer.update();
        }
    }

    public int getStockCount() {
        return stockCount;
    }

    public void setStockCount(int newStockAdded) {
        if (stockCount == 0) {
            notifySubscribers();
        }
        stockCount += newStockAdded;
    }
}

