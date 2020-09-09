import unittest
from car import Car

import os, shutil
        

class TestCar(unittest.TestCase):

    def setUp(self):
        shutil.copy("registered_cars.txt", "backup_registered_cars.txt")

    def test_add_car_number_in_class(self):
        a = Car('AAA-002')
        self.assertEqual(a.car_number, 'AAA-002', "Should be AAA-002")
        
    def test_add_car_number_in_instance(self):
        b = Car()
        b.car_number = "AAA-001"
        self.assertEqual(b.car_number, "AAA-001", "Should be AAA-001")
        
    def test_registered_cars(self):
        a = Car('AAA-001')
        b = Car('AAA-002')
        self.assertEqual(b.registered_cars, ['AAA-001', 'AAA-002'], "Should be ['AAA-001', 'AAA-002']")

    def test_car_count(self):
        a = Car('AAA-001')
        b = Car('AAA-002')
        self.assertEqual(b.car_count, 2, "Should be 2")

    # def test_car_number_regex(self):
    #     self.assertEqual(Car('1AA-00A').car_number_not_valid(), "Not a valid number", "Should be 'Not a valid number'")
        


    def tearDown(self):
        shutil.copy("backup_registered_cars.txt", "registered_cars.txt")
        os.remove("backup_registered_cars.txt")
        


if __name__ == '__main__':
    unittest.main()