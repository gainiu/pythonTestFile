import unittest


class Employee():
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, raises=5000):
        self.annual_salary += raises


class EmployeeTestCase(unittest.TestCase):
    '''针对Employee类的测试'''

    def setUp(self):
        '''创建一个雇员对象'''
        self.my_employee = Employee('xiao', 'min', 200000)
        self.raises = 10000
        self.default_salary = 205000
        self.custom_salary = 210000

    def test_give_default_raise(self):
        '''测试默认增长年薪5000'''
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.annual_salary, self.default_salary)

    def test_give_custom_raise(self):
        '''测试自定义年薪增长值'''
        self.my_employee.give_raise(self.raises)
        self.assertEqual(self.my_employee.annual_salary, self.custom_salary)


unittest.main()
