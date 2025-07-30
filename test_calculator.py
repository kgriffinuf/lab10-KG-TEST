import unittest
from calculator import *
import math

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ####### Partner 1
    def test_multiply(self): # 3 assertions
        # check if the results are equal to the expected
        expected = self.a * self.b
        result = self.mul
        self.assertEqual(result, expected)

        # check if result is an integer
        self.assertIsInstance(result, int)

        # verify if the product(result) is greater than both variables a and b
        self.assertTrue(result >= self.a and result >= self.b)

    def test_divide(self): # 3 assertions
        # ensure a is not equal to zero
        assert self.a != 0, "Zero Division Error"

        # ensure the result of div method is equal to the expected
        expected = self.b / self.a
        result = self.div
        self.assertEqual(result, expected)

        # ensure the result is a float
        self.assertIsInstance(result, float)
    #########################

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ####### Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            math.log(self.a, self.b)
        # call log function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
        with self.assertRaises(ValueError):
            self.a != 0
        with self.assertRaises(ValueError):
            self.b != 0
        expected = math.hypot(self.a, self.b)
        result = self.hypotenuse
        self.assertEqual(result, expected)


    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #    square_root(NUM)
        # Test basic function
        expected = math.sqrt(self.a)
        result = math.sqrt(self.a)

        # a is greater than zero
        with self.assertRaises(ValueError):
            self.a < 0

        # result is a float
        self.assertIsInstance(result, float)

        # value error for assertRaises
        with self.assertRaises(ValueError):
            math.sqrt(self.a, self.b)

    #########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()