#  File: employee.py
#  Description: constructing employees with different salaries
#  Student Name: Sneha Kamal
#  Student UT EID: sk52223
#  Course Name: CS 313E
#  Unique Number: 52520
#  Date Created: 09/19/2022
#  Date Last Modified: 09/19/2022

import sys
class Employee:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.id = kwargs.get('id')
        self.salary = kwargs.get('salary', "None")
    def __str__(self):
        return f"Employee \n {self.name}, {self.id}, {self.salary}"


class Permanent_Employee(Employee):
    def __init__(self, **kwargs):
        super(Permanent_Employee, self).__init__(**kwargs)
        self.benefits = kwargs.get('benefits')
    def cal_salary(self):
        if self.benefits == ["health_insurance"]:
            return self.salary * 0.9
        elif self.benefits == ["retirement"]:
            return self.salary * 0.8
        else:
            return self.salary * 0.7
    def __str__(self):
        return f"Permanent_Employee \n {self.name}, {self.id}, {self.cal_salary()}, {self.benefits}"


class Manager(Employee):
    def __init__(self, **kwargs):
        super(Manager, self).__init__(**kwargs)
        self.bonus = kwargs.get('bonus')
    def cal_salary(self):
        return self.salary + self.bonus
    def __str__(self):
        return f"Manager \n {self.name}, {self.id}, {self.cal_salary()}"

class Temporary_Employee(Employee):
    def __init__(self, **kwargs):
        super(Temporary_Employee, self).__init__(**kwargs)
        self.hours = kwargs.get('hours')
    def cal_salary(self):
        return self.salary * self.hours
    def __str__(self):
        return f"Temporary_Employee \n {self.name}, {self.id}, {self.cal_salary()}"


class Consultant(Temporary_Employee):
    def __init__(self, **kwargs):
        super(Consultant, self).__init__(**kwargs)
        self.travel = kwargs.get('travel')
    def cal_salary(self):
        return self.salary * self.hours + (self.travel * 1000)
    def __str__(self):
        return f"Consultant \n {self.name}, {self.id}, {self.cal_salary()}"


class Consultant_Manager(Consultant, Manager):
    def __init__(self,  **kwargs):
        super(Consultant_Manager, self).__init__(**kwargs)
    def cal_salary(self):
        return self.salary * self.hours + (self.travel * 1000) + self.bonus
    def __str__(self):
        return f"Consultant \n {self.name}, {self.id}, {self.cal_salary()}"


###### DO NOT CHANGE THE MAIN FUNCTION ########
def main():
    chris = Employee(name="Chris", id="UT1")
    print(chris, "\n")
    emma = Permanent_Employee(name="Emma", id="UT2", salary=100000,
benefits=["health_insurance"])
    print(emma, "\n")
    sam = Temporary_Employee(name="Sam", id="UT3", salary=100,  hours=40)
    print(sam, "\n")
    john = Consultant(name="John", id="UT4", salary=100, hours=40, travel=10)
    print(john, "\n")
    charlotte = Manager(name="Charlotte", id="UT5", salary=1000000, bonus=100000)
    print(charlotte, "\n")
    matt = Consultant_Manager(name="Matt", id="UT6", salary=1000, hours=40,
travel=4, bonus=10000)
    print(matt, "\n")
    ###################################
    print("Check Salaries")
    print("Emma's Salary is:", emma.cal_salary(), "\n")
    emma.benefits = ["health_insurance"]
    print("Emma's Salary is:", emma.cal_salary(), "\n")
    emma.benefits = ["retirement", "health_insurance"]
    print("Emma's Salary is:", emma.cal_salary(), "\n")
    print("Sam's Salary is:", sam.cal_salary(), "\n")
    print("John's Salary is:", john.cal_salary(), "\n")
    print("Charlotte's Salary is:", charlotte.cal_salary(), "\n")
    print("Matt's Salary is:",  matt.cal_salary(), "\n")
if __name__ == "__main__":
  main()