package ObserverDesignPattern.Observer;

import ObserverDesignPattern.Observable.StockObservable;

public class EmailAlertObserverImpl implements NotificationAlertObserver {
    String emailId;
    StockObservable observable;

    public EmailAlertObserverImpl(String emailId, StockObservable observable) {
        this.emailId = emailId;
        this.observable = observable;
    }

    public void update() {
        sendMail(emailId, msg:"product in stock hurry");
    }

    public void sendMail(String emailId, String msg) {
        System.out.println("Mail sent");
    }
}