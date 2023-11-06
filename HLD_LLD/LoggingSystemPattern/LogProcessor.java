public abstract class LogProcessor {
    public static int INFO = 1;
    public static int DEBUG = 2;
    public static int ERROR = 3;

    LogProcessor nextLogProcessor;

    public LogProcessor(LogProcessor logprocessor){
        this.nextLogProcessor = logprocessor;
    }

    public void log(int info , String message){
        if (nextLogProcessor != null) {
            nextLogProcessor.log(info  , message);
        }
    }
}


class DebugLogProcessor extends LogProcessor {
    DebugLogProcessor(LogProcessor nextLogProcessor){
        super(nextLogProcessor);
    }

    public void log(int loglLevel , String message){
        if(loglLevel == DEBUG){
            System.out.println("DEBUG = " , message)
        } else {
            super.log(loglLevel , message);
        }
        
    }
}

class ErrorLogProcessor extends LogProcessor {
    ErrorLogProcessor(LogProcessor nextLogProcessor){
        super(nextLogProcessor);
    }

    public void log(int loglLevel , String message){
        if(loglLevel == ERROR){
            System.out.println("ERROR = " , message)
        } else {
            super.log(loglLevel , message);
        }
        
    }
}

class InfoLogProcessor extends LogProcessor {
    InfoLogProcessor(LogProcessor nextLogProcessor){
        super(nextLogProcessor);
    }

    public void log(int loglLevel , String message){
        if(loglLevel == INFO){
            System.out.println("INFO = " , message)
        } else {
            super.log(loglLevel , message);
        }
        
    }
}
public class Main {
    public static void main(String args){
        LogProcessor logObject = new InfoLogProcessor(new DebugLogProcessor(new ErrorLogProcessor(null)));

        logObject.log(logprocessor.ERROR  , "exception");
        logObject.log(logprocessor.DEBUG  , "need to debug");
        logObject.log(logprocessor.INFO  , "info");
    }
}