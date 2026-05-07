import unittest
from largestnumber import addition
from largestnumber import multiply
from largestnumber import substraction

class TestAddition(unittest.TestCase):


    def test_that_method_calaculation_the_sum_of_two_numbers(self):
        first_number = 9
        second_number = 5
        expected = 14
        actual = addition(first_number, second_number)
        self.assertEqual(actual, expected)

    def test_the_product_of_two_numbers(self):
        first_number = 9
        second_number = 5
        expected = 45
        actual = multiply(first_number, second_number)
        self.assertEqual (actual,  expected)

    def test_the_difference_of_two_numbers(self):
        first_number = 9 
        second_number = 5
        expected = 4
        actual = substraction(first_number, second_number)
        self.assertEqual(actual, expected)
