// When we have to hide the system complexities from client we use Facade
// Facade is not mandatory

class EmployeeDao {
    public void insert() {
        // inserts into DB
    }
    public void setName() {
        // update DB
    }

    public getEmpDetails( int empId ){
        // return Employee()
    }
}

class EmployeeFacade {
    EmployeeDao employeeDAO;
    public EmployeeFacade(){
        employeeDAO = new EmployeeDao();
    }

    public void insert(){
        employeeDAO.insert();
    }
    public Employee getEmpDetails(empId){
        return employeeDAO.getEmpDetails(empId);
    }
}