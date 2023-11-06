// Used in Proxy Serveers
// used in caching
// Pre and Post processing\

public interface EmployeeDao {
    public void create( String client  , EmployeeDo obj) throws Exception;
    public void create( String client , int employeeId ) throws Exception;
    public EmployeeDo get(String client , int employeeId) throws Exception;

     
}

public class EmployeeImpl implements EmployeeDao {

    @Override
    public void create(String client , EmployeeDo obj) throws Exception {
        System.out.println("Created new row in the EMployee Table");        
    }
    @Override
    public void delete(String client , int employeeId) throws Exception {
        System.out.println("deleted row in the EMployee Table");        
    }

    @Override
    public EmployeeDo get(String client , int employeeId) throws Exception {
        System.out.println("Fetchiing data from DB");        
        return new EmployeeDo();
    }
}

public class EmployeeDaoProxy implements EmployeeDao {
    EmployeeDao emplployeeDaoObj;
    EmployeeDaoProxy(){
        emplployeeDaoObj = new EmployeeImpl();
    }

    @Override
    public void create(String client , EmployeeDo obj) throws Exception {
        if (client.equals("ADMIN")) {
            emplployeeDaoObj.create(client , obj);
            return;
        }
        throw new Exception("Acceess Denied");
    }

    @Override
    public void delete(String client , int employeeId) throws Exception {
        if (client.equals("ADMIN")) {
            emplployeeDaoObj.delete(client , employeeId);
            return;
        }
        throw new Exception("Acceess Denied");
    }

    @Override
    public EmployeeDo get(String client , int employeeId) throws Exception {
        if (client.equals("ADMIN") || client.equals("USER")) {
            return emplployeeDaoObj.get(client , employeeId);            
        }
        throw new Exception("Acceess Denied");
    }
}

public class ProxyDesignPattern {
    public static void main(){
        try{
            EmployeeDao  empTableObj = new EmployeeDaoProxy();
            empTableObj.create("USER" , new EmployeeDo());
        } catch(Exception e){
            System.out.print(e.getMessage());
        }
    }
}