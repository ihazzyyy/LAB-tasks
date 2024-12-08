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