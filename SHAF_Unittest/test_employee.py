import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    version='mama'
    def setUp(self):
        self.emp_1=Employee('Corey', 'Shafer',50000)
        self.emp_2=Employee('Sue', 'Smith', 60000)
    def tearDown(self):
        pass 
    @classmethod
    def setUpClass(cls):
        pass
    @classmethod
    def tearDownClass(cls):
        pass
    def test_email(self):
        self.assertEqual(self.emp_1.email, 'Corey.Shafer@email.com')
        self.assertEqual(self.emp_2.email, 'Sue.Smith@email.com')
        self.emp_1.first='John'
        self.emp_2.last='Adablyon'
        self.assertEqual(self.emp_1.email,'John.Shafer@email.com')
        self.assertEqual(self.emp_2.email,'Sue.Adablyon@email.com')
    def test_fullname(self):
        self.assertEqual(self.emp_1.fullname, 'Corey Shafer')
        self.assertEqual(self.emp_2.fullname, 'Sue Smith')
        self.emp_1.first='John'
        self.emp_2.last='Adablyon'  
        self.assertEqual(self.emp_1.fullname, 'John Shafer')
        self.assertEqual(self.emp_2.fullname, 'Sue Adablyon')
    def test_apply_raise(self):
        self.emp_1.apply_raise()
        self.emp_2.apply_raise() 
        self.assertEqual(self.emp_1.pay, 50000*1.05)
        self.assertEqual(self.emp_2.pay, 60000*1.05)

if __name__=='__main__':
    unittest.main()     