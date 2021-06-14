import unittest
from controller import *

class TestingFunctions(unittest.TestCase):
#Testing that employee with id 1 and employee with id 4 are not the same
    def testing_get_employee_method(self):
        self.assertNotEqual(get_employee(1),get_employee(5))

#Testing that get_teim method will return none if we ask for a item that doesnt exist
    def testing_get_item_method(self):
        self.assertIsNone(get_item(2120))

#Testing that employee and item are not the same table
    def testing_get_employee_and_get_item_method(self):
        self.assertNotEqual(get_employee(1),get_item(4))


if __name__ == 'main':
        unittest.main()