'''
    Initial validation class
'''
class Validate:
    """
        Hello There class to verify configuration
    """
    def hi_there(self, fred=False):
        '''
            Just return a string
        '''
        if fred is True:
            res = "Fred was here"
        else:
            res = 'Hi There'
        return res
