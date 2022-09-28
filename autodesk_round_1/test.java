public class Employee {
    private final int id;
    private final String name;
    private final Date doj;

    public Employee(int id, String name, Date doj) {
        this.id = id;
        this.name = name;
        this.doj = doj;
    }

    // no setter only getters
    public Date getDoj() {
        return this.doj;
    }
}

/////////////////////////////////////

GET /customer?name={name}

@RestController
CustomerController

@Autowired
CustomerService

@GetMapping("/customer", QueryParams name)

CustomerService
/getCustomer
if name = name {}

Entity
id
name, ...

FilterInterface

NameFilter impl FilterInterface
PincodeFilter impl FilterInterface

FilterFactory.create()