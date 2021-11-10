import sqlite3
from empolyee import Employee
conn = sqlite3.connect('employee.db')
cursor = conn.cursor()

cursor.execute("""DROP TABLE IF EXISTS employees""")
cursor.execute("""CREATE TABLE employees (
                 first text,
                 last text,
                 pay integer)
                 """)
'''
cursor.execute("""INSERT INTO employees VALUES 
                 ('Corey','Shafer','50000')""")
cursor.execute("""INSERT INTO employees VALUES 
                 ('mary','Shafer','50000')""")
cursor.execute("""SELECT * FROM employees""")
print(cursor.fetchone())
print(cursor.fetchone())

emp_1 = Employee('John','Doe',80000)
emp_2 = Employee('Nancy','Doe',30000)
emp_3 = Employee('Gary','Doe',50000)

#cursor.execute("INSERT INTO employees VALUES('{}', '{}', {})".format(emp_1.first, emp_1.last, emp_1.pay))                #tak nie wolno
cursor.execute("INSERT INTO employees VALUES (?,?,?)", (emp_2.first, emp_2.last, emp_2.pay))
cursor.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp_3.first, 'last': emp_3.last, 'pay': emp_3.pay})
conn.commit()
conn.close() 
'''

def insert_emp(emp):
    with conn:
        cursor.execute("INSERT INTO employees VALUES (?,?,?)", (emp.first, emp.last, emp.pay))
def get_emps_by_name(name):
    cursor.execute('SELECT * FROM employees WHERE first = :first', {'first': name})
    return cursor.fetchall()	
def update_pay(emp,number):
    with conn:
        cursor.execute("UPDATE employees SET pay=:pay WHERE first=:first AND last=:last", {'first': emp.first, 'last': emp.last, 'pay': number})
def remove_emp(emp):
    with conn:
        cursor.execute("DELETE FROM employees WHERE first=:first AND last=:last ", {'first': emp.first, 'last': emp.last})

emp_1 = Employee('John','Doe',80000)
emp_2 = Employee('Nancy','Doe',30000)
emp_3 = Employee('Gary','Doe',50000)
insert_emp(emp_1)
insert_emp(emp_2)
insert_emp(emp_3)

emps = get_emps_by_name(emp_1.first)
print(emps)

update_pay(emp_2, 23000)
remove_emp(emp_1)

emps = get_emps_by_name(emp_2.first)
print(emps)

conn.close()

