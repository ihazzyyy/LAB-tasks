import csv

class Employee:
    def __init__(self, name, age, salary):
        self.__name = name 
        self.__age = age
        self.__salary = salary

   
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

     
    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age >= 0:
            self.__age = age  
        else:
            print('Enter appropriate age / age cannot be negative')

    
    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary >= 0:
            self.__salary = salary  
        else:
            print('Salary cannot be negative')

class Manager(Employee):
    def __init__(self, name, age, salary, department):
        super().__init__(name, age, salary)
        self.__department = department
        
    
    def get_department(self):
        return self.__department

    def set_department(self, department):
        self.__department = department

class Worker(Employee):
    def __init__(self, name, age, salary, hours_worked):
        super().__init__(name, age, salary)
        self.__hours_worked = hours_worked

    
    def get_hours_worked(self):
        return self.__hours_worked
        
    def set_hours_worked(self, hours_worked):  
        if hours_worked >= 0:  
            self.__hours_worked = hours_worked
        else:
            print('Hours cannot be negative / enter appropriate number')

def save(filename, employees):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Age', 'Salary', 'Department', 'Hours worked'])  
        for employee in employees:
            if isinstance(employee, Manager):
                writer.writerow([employee.get_name(), employee.get_age(), employee.get_salary(), employee.get_department(), 'N/A'])  
            elif isinstance(employee, Worker):
                writer.writerow([employee.get_name(), employee.get_age(), employee.get_salary(), 'N/A', employee.get_hours_worked()])  

def load(filename):
    employees = []

    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # skips header
        for row in reader:
            name, age, salary, department, hours_worked = row
            age = int(age)
            salary = float(salary)
            if department != 'N/A':
                employees.append(Manager(name, age, salary, department))
            else:
                employees.append(Worker(name, age, salary, float(hours_worked)))  
    return employees

def add(employees, type):
    name = input('Enter the Name: ')
    age = int(input('Enter the Age: '))
    salary = float(input('Enter the Salary: '))

    if type == 'Manager':
        department = input('Enter the department: ')
        employees.append(Manager(name, age, salary, department))
    elif type == 'Worker':
        hours_worked = float(input('Enter the number of hours worked: '))
        employees.append(Worker(name, age, salary, hours_worked))
    else:
        print('Enter the type correctly either Manager/Worker!')  

def update(employees):
    name = input('Enter the name to update: ')
    for emp in employees:
        if emp.get_name() == name:
            emp.set_name(input('Enter the new Name: '))  
            emp.set_age(int(input('Enter the new Age: ')))  
            emp.set_salary(float(input('Enter the new Salary: ')))  
            if isinstance(emp, Manager):  
                emp.set_department(input('Enter the new department: '))
            elif isinstance(emp, Worker):  
                emp.set_hours_worked(float(input('Enter the updated number of hours worked: ')))
            print('UPDATED SUCCESSFULLY!')
            return
    print(f'No employee found with the name {name}!')

def delete(employees):
    name = input('Enter the name of the employee to erase data: ')
    for emp in employees:
        if emp.get_name() == name:  
            employees.remove(emp)
            print('Employee deleted successfully!')
            return
    print(f'No employee found with the name {name}!')

def display(employees):
    for emp in employees:
        print(f'Name: {emp.get_name()}, Age: {emp.get_age()}, Salary: {emp.get_salary()}')
        if isinstance(emp, Manager):  
            print(f'Department: {emp.get_department()}')  
        elif isinstance(emp, Worker):  
            print(f'Hours Worked: {emp.get_hours_worked()}')  
        print('-' * 30)

def main():
    employees = []
    filename = 'assignment10.csv'

    while True:
        print("\n1. Add Manager")
        print("2. Add Worker")
        print("3. Display Employees")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Save to File")
        print("7. Load from File")
        print("8. Exit")

        choice = input('Enter your choice: ')
        if choice == '1':
            add(employees, "Manager")
        elif choice == '2':
            add(employees, "Worker")
        elif choice == '3':
            display(employees)
        elif choice == '4':
            update(employees)
        elif choice == '5':
            delete(employees)
        elif choice == '6':
            save(filename, employees)
            print("Employees saved to file.")
        elif choice == '7':
            employees = load(filename)
            print("Employees loaded from file.")
        elif choice == '8':
            break
        else:
            print("Invalid choice! Please try again.")

main()
