'''
    Test setup
'''

import unittest
from src.verify.validate import Validate

class TestValidate(unittest.TestCase):
    """
        Testing class for instalation validation
    """
    def test_hello_there_default(self):
        '''
            Instantiate and run first method
        '''
        class_instance = Validate()
        res = class_instance.hi_there()
        self.assertEqual(res, 'Hi There')

    def test_hello_there_false(self):
        '''
            Instantiate and run first method
        '''
        class_instance = Validate()
        res = class_instance.hi_there(fred=False)
        self.assertEqual(res, 'Hi There')

    def test_hello_there_true(self):
        '''
            Instantiate and run first method
        '''
        class_instance = Validate()
        res = class_instance.hi_there(fred=True)
        self.assertEqual(res, 'Fred was here')

    if __name__ == '__main__':
        unittest.main()
