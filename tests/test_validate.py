'''
    Test setup
'''
from pytest_workshop.validate import Validate

def test_hello_there_default():
    '''
        Instantiate and run first method
    '''
    class_instance = Validate()
    res = class_instance.hi_there()
    assert res == 'Hi There'

def test_hello_there_false():
    '''
        Instantiate and run first method
    '''
    class_instance = Validate()
    res = class_instance.hi_there(fred=False)
    assert res == 'Hi There'

def test_hello_there_true():
    '''
        Instantiate and run first method
    '''
    class_instance = Validate()
    res = class_instance.hi_there(fred=True)
    assert res == 'Fred was here'
