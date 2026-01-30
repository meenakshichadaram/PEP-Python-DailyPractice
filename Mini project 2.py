"""
The system should calculate salary for different types pf emplyees using all oops concepts
Employee - Abstract class
Full Time employee - Child class
Part time employee - child class
salary - encapsulated data
payroll system - controller(HAS-A)
output-
Employee created
Salary:50000
Employee Created
Salary:40000
"""
class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    def calculate_salary(self):
        pass
class FullTimeEmployee(Employee):
    def __init__(self, emp_id, name, monthly_salary):
        super().__init__(emp_id, name)
        self._monthly_salary = monthly_salary   # fixed spelling

    def calculate_salary(self):
        return self._monthly_salary


class PartTimeEmployee(Employee):
    def __init__(self, emp_id, name, hours_worked, rate_per_hour):
        super().__init__(emp_id, name)
        self._hours_worked = hours_worked
        self._rate_per_hour = rate_per_hour

    def calculate_salary(self):
        return self._hours_worked * self._rate_per_hour


class PayrollApp:
    def __init__(self):        
        self.employee = None

    def create_employee(self, emp_type):
        if emp_type == "FullTime":
            self.employee = FullTimeEmployee(1, "Amit", 50000)
        else:
            self.employee = PartTimeEmployee(2, "Neha", 80, 500)
        return "-> Employee Created"

    def get_salary(self):
        return self.employee.calculate_salary()

app = PayrollApp()
print(app.create_employee("FullTime"))
print("Salary:", app.get_salary())

app2 = PayrollApp()
print(app2.create_employee("PartTime"))
print("Salary:", app2.get_salary())

