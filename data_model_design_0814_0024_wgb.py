# 代码生成时间: 2025-08-14 00:24:29
import numpy as np


class Person:
    """
    A simple data model class representing a person.
    Attributes:
        name (str): The name of the person.
        age (int): The age of the person.
    """
    def __init__(self, name, age):
        """Initialize a new Person instance."""
        self.name = name
        self.age = age

    def __str__(self):
        """Return a string representation of the Person."""
        return f"Person(name={self.name}, age={self.age})"

    def is_adult(self):
        """Check if the person is an adult (18 or older)."""
        return self.age >= 18



class Employee(Person):
    """
    A subclass of Person, representing an employee.
    Attributes:
        employee_id (int): Unique identifier for the employee.
        department (str): The department where the employee works.
    """
    def __init__(self, name, age, employee_id, department):
        """Initialize a new Employee instance."""
        super().__init__(name, age)
        self.employee_id = employee_id
        self.department = department

    def __str__(self):
        """Return a string representation of the Employee."""
        return (f"Employee(name={self.name}, age={self.age}, "
                f"employee_id={self.employee_id}, department={self.department})")



# Example usage and error handling
if __name__ == '__main__':
    try:
        # Create a person
        person = Person("John Doe", 30)
        print(person)

        # Check if the person is an adult
        if person.is_adult():
            print(f"{person.name} is an adult.")
        else:
            print(f"{person.name} is not an adult.")

        # Create an employee
        employee = Employee("Jane Smith", 25, 12345, "HR")
        print(employee)

    except TypeError as e:
        print(f"An error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
