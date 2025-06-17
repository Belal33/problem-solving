from table_manager import DBModel


class Employee(DBModel):
    first_name: str
    last_name: str
    age: int
    department: str
    salary: float
    managed_department: str = ""


class Emp:
    first_name: str
    last_name: str
    age: str
    department: str
    salary: str
    __employees: list["Employee"] = []

    def __init__(self, first_name, last_name, age, department, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.department = department
        self.salary = salary

    def add(self):
        emp = Employee(
            first_name=self.first_name,
            last_name=self.last_name,
            age=self.age,
            department=self.department,
            salary=self.salary,
            managed_department=self.department,
        )
        emp.save()

    @staticmethod
    def transfer(emp_id: int, new_department: str):
        emp = Employee.get_by_pk(emp_id)
        if emp:
            emp.update(department=new_department)
            emp.show()
        else:
            print("Employee not found")

    @classmethod
    def fire(cls, emp_id: int):
        emp = Employee.get_by_pk(emp_id)
        if emp:
            if emp.managed_department == "":

                emp.delete()

            else:
                print("Employee is manager can't be fired")
        else:
            print("Employee not found")
        return emp

    @staticmethod
    def show(emp_id: int):
        emp = Employee.get_by_pk(emp_id)
        if emp:
            emp.show()
        else:
            print("Employee not found")

    @staticmethod
    def list_employees():
        Employee.list_all()


class Manager(Emp):
    managed_department = None

    def __init__(
        self, first_name, last_name, age, department, salary, managed_department
    ):
        super().__init__(first_name, last_name, age, department, salary)
        self.managed_department = managed_department

    def add(self):
        emp = Employee(
            first_name=self.first_name,
            last_name=self.last_name,
            age=self.age,
            department=self.department,
            salary=self.salary,
            managed_department=self.managed_department,
        )
        emp.save()




def main():
    while True:
        print("Menu:")
        print("1. Add Employee (add)")
        print("2. List All Employees (list)")
        print("3. Get Employee by ID (get)")
        print("4. Fire Employee (fire)")
        print("5. Transfer Employee (transfer)")
        print("4. Exit (q)")

        choice = input("Enter your choice: ").strip().lower()

        if choice == "add":
            try:
                isManager = (
                    True
                    if input(" If manager press “m”/ if employee press ‘e’: ") == "m"
                    else False
                )
                first_name = input("First Name: ")
                last_name = input("Last Name: ")
                age = int(input("Age: "))
                department = input("Department: ")
                salary = float(input("Salary: "))
                emp = Manager(
                    first_name=first_name,
                    last_name=last_name,
                    age=age,
                    department=department,
                    salary=salary,
                    managed_department=department if isManager else "",
                ).add()
                print("Employee added successfully.")
            except ValueError as e:
                print(f"Error: {e}. Please enter valid data.")
                continue

        elif choice == "list":
            Emp.list_employees()

        elif choice == "get":
            Emp.show(int(input("Enter Employee ID: ")))
        elif choice == "fire":
            Emp.fire(int(input("Enter Employee ID: ")))

        elif choice == "transfer":
            Emp.transfer(
                int(input("Enter Employee ID: ")), input("Enter New Department: ")
            )

        elif choice == "q":
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
