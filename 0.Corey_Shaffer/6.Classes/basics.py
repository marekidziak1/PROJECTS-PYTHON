class Employee:
    raise_amount=1.04
    num_of_employees=0
    def __init__(self, first, last,  pay):
        self.first=first
        self.last=last
        self.pay=pay
        Employee.num_of_employees+=1
    
    @property
    def email(self):
        return f'{self.first.lower()}.{self.last.lower()}@companyname.com'
    
    @property
    def fullname(self):
        return f'{self.first} {self.last}'
    
    @fullname.setter
    def fullname(self, name):
        self.first, self.last = name.split(" ")

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount=amount

class Developer(Employee):
    def __init__(self, first, last,  pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang=prog_lang

class Manager(Employee):
    def __init__(self, first, last,  pay, employees = None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees=[]
        else:
            self.employees=employees
    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


emp_1=Employee('Marek', 'Darek', 30_000)
emp_2=Employee('Darek', 'Marek', 60_000)

dev_1=Developer('Marek', 'Darek', 30_000, 'Python')
mgr_1 = Manager('Sue','Smith',90_000, [dev_1])

print(mgr_1.email) 


'''
print(emp_1.fullname())
print(Employee.fullname(emp_1))
print(Employee.num_of_employees)
'''