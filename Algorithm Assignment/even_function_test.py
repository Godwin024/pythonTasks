import unittest
import even_function

class even_function_test(unittest.TestCase):
    
    def test_that_the_number_is_Even(self):
        number = 2
        self.assertTrue(even_function.even_number(number))
        
